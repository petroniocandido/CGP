#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash,redirect, url_for, session
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField, PasswordField
from wtforms.validators import DataRequired

from CGP.ControllerBase import usuarioLogado
from CGP.DomainModel import TipoLog, Log, Pessoa, Salvar, Remover, appendLog

login = Blueprint('login', __name__)


class LoginForm(Form):
    login = StringField("Login", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    

@login.route('/login/', methods=('GET', 'POST'))
def efetuarLogin():
    if request.method == 'POST':
        form = LoginForm(formdata=request.form)
        if form.validate():
            pessoa = Pessoa.query.filter(Pessoa.email_Institucional == form.login.data).first()
            if pessoa == None:
                appendLog(TipoLog.ERRO, "Login incorreto: " + form.login.data, None)
                flash('E-mail ou senha incorretos!', 'danger')
            else:
                if pessoa.checar_senha(form.senha.data):
                    session["usuario_id"] = pessoa.id
                    session["usuario_nome"] = pessoa.email_Institucional
                    appendLog(TipoLog.SUCESSO,"Login bem sucedido",pessoa)
                    return redirect(url_for('pessoas.Listar'))
                else:
                    appendLog(TipoLog.ERRO, "Senha incorreta: " + form.login.data, None)
                    flash('E-mail ou senha incorretos!', 'danger')
    else:
        form = LoginForm()

    return render_template('login.html', form=form)


@login.route('/logout/', methods=('GET','POST'))
def efetuarLogout():
    pessoa = usuarioLogado()
    appendLog(TipoLog.SUCESSO, "Logout bem sucedido", pessoa)
    form = LoginForm()
    session["usuario_id"] = None
    session["usuario_nome"] = None
    return render_template('login.html', form=form)
