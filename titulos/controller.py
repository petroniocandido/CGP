#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms_alchemy import ModelForm, ModelFormField, ModelFieldList
from wtforms import StringField, HiddenField, SelectField, FormField, BooleanField, FieldList
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Optional

from ControllerBase import SalvarEntidade,RemoverEntidade, logsAuditoria, requer_autenticacao_autorizacao
from DomainModel import Pessoa, Titulo

titulos = Blueprint('titulos', __name__)


class TituloForm(ModelForm):
    class Meta:
        model = Titulo
        include = ['id', 'pessoa_id']


@titulos.route('/editar/<int:pessoa_id>,<int:titulo_id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Editar(pessoa_id=0, titulo_id=0):
    if titulo_id == 0:
        titulo = Titulo()
        titulo.id = 0
        titulo.pessoa_id = pessoa_id
    else:
        titulo = Titulo.query.filter(Titulo.id == titulo_id).first()

    if request.method == 'POST':
        form = TituloForm(formdata=request.form)
        form.populate_obj(titulo)

        SalvarEntidade(form,titulo)
    else:
        form = TituloForm(obj=titulo)

    return render_template('editarTitulo.html', form=form, auditoria = logsAuditoria(titulo))


@titulos.route('/remover/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Remover(id):
    titulo = Titulo.query.filter(Titulo.id == id).first()
    pessoa_id = titulo.pessoa_id
    RemoverEntidade(titulo)
    return redirect(url_for('pessoas.Editar', id=pessoa_id))
