#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from ControllerBase import SalvarEntidade,RemoverEntidade

from DomainModel import Permissao

permissoes = Blueprint('permissoes', __name__)


class PermissaoForm(ModelForm):
    class Meta:
        model = Permissao
        include = ['id']


@permissoes.route('/listar/')
def Listar():
    permissoes = Permissao.query.all()
    return render_template('listarPermissoes.html', listagem=permissoes)


@permissoes.route('/editar/<int:id>', methods=('GET', 'POST'))
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

    return render_template('editarPermissao.html', form=form)


@permissoes.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    permissao = Permissao.query.filter(Permissao.id == id).first()
    RemoverEntidade(permissao)
    return redirect(url_for('.Listar'))

