#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash,redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from CGP.ControllerBase import SalvarEntidade,RemoverEntidade, requer_autenticacao_autorizacao

from CGP.DomainModel import Log, Pessoa

logs = Blueprint('logs', __name__)


class LogForm(ModelForm):
    class Meta:
        model = Log
        include = ['id']
    

@logs.route('/listar/')
@requer_autenticacao_autorizacao
def Listar():
    logs = Log.query.order_by(Log.data.desc()).all()
    return render_template('listarLogs.html', listagem=logs)


@logs.route('/editar/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Editar(id=0,tab="geral"):
    if id == 0:
        log = Log()
        log.id = 0
    else:
        log = Log.query.filter(Log.id == id).first()

    if request.method == 'POST':
        form = LogForm(formdata=request.form)
        form.populate_obj(log)

        SalvarEntidade(form,log)
    else:
        form = LogForm(obj=log)

    if log.pessoa_id != 0:
        pessoa = Pessoa.query.get(log.pessoa_id)
    else:
        pessoa = None

    return render_template('editarLog.html', tab=tab, form=form, pessoa = pessoa)


@logs.route('/remover/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Remover(id):
    log = Log.query.filter(Log.id == id).first()
    RemoverEntidade(log)
    return redirect(url_for('.Listar'))

