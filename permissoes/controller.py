#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import Permissao, Salvar, Remover

permissoes = Blueprint('permissoes', __name__)


class PermissaoForm(ModelForm):
    class Meta:
        model = Permissao
        include = ['id']


@permissoes.route('/listar/')
def permissoesListar():
    permissoes = Permissao.query.all()
    return render_template('listarPermissoes.html', listagem=permissoes)


@permissoes.route('/editar/<int:id>', methods=('GET', 'POST'))
def permissaoEditar(id=0):
    if id == 0:
        permissao = Permissao()
        permissao.id = 0
    else:
        permissao = Permissao.query.filter(Permissao.id == id).first()

    if request.method == 'POST':
        form = PermissaoForm(formdata=request.form)

        if form.validate():
            form.populate_obj(permissao)
            if Salvar(permissao):
                flash('Salvo com sucesso!', 'success')
            else:
                flash('Falha ao salvar!', 'danger')
    else:
        form = PermissaoForm(obj=permissao)

    return render_template('editarPermissao.html', form=form)


@permissoes.route('/remover/<int:id>', methods=('GET', 'POST'))
def permissaoRemover(id):
    permissao = Permissao.query.filter(Permissao.id == id).first()
    if Remover(permissao):
        flash('Removido com sucesso!', 'success')
    else:
        flash('Falha ao remover!', 'danger')
    permissoes = Permissao.query.all()
    return render_template('listarPermissoes.html', listagem=permissoes)

