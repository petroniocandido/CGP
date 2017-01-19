#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from CGP.ControllerBase import SalvarEntidade,RemoverEntidade,logsAuditoria, requer_autenticacao_autorizacao

from CGP.DomainModel import Permissao

permissoes = Blueprint('permissoes', __name__)


class PermissaoForm(ModelForm):
    class Meta:
        model = Permissao
        include = ['id']


@permissoes.route('/listar/')
@requer_autenticacao_autorizacao
def Listar():
    permissoes = Permissao.query.all()
    return render_template('listarPermissoes.html', listagem=permissoes)


@permissoes.route('/editar/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Editar(id=0):
    if id == 0:
        permissao = Permissao()
        permissao.id = 0
    else:
        permissao = Permissao.query.filter(Permissao.id == id).first()

    if request.method == 'POST':
        form = PermissaoForm(formdata=request.form)
        form.populate_obj(permissao)

        SalvarEntidade(form,permissao)
    else:
        form = PermissaoForm(obj=permissao)

    return render_template('editarPermissao.html', form=form, auditoria = logsAuditoria(permissao))


@permissoes.route('/remover/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Remover(id):
    permissao = Permissao.query.filter(Permissao.id == id).first()
    RemoverEntidade(permissao)
    return redirect(url_for('.Listar'))

