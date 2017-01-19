#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from CGP.ControllerBase import SalvarEntidade, RemoverEntidade, logsAuditoria, requer_autenticacao_autorizacao
from CGP.DomainModel import Setor, Campus

setores = Blueprint('setores', __name__)


class SetorForm(ModelForm):
    class Meta:
        model = Setor
        include = ['id']

    campus_id = SelectField('Campus', coerce=int, choices=[(c.id, c.sigla) for c in Campus.query.order_by('sigla')])


@setores.route('/listar/')
@requer_autenticacao_autorizacao
def Listar():
    setores = Setor.query.all()
    return render_template('listarSetores.html', listagem=setores)


@setores.route('/editar/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Editar(id=0):
    if id == 0:
        setor = Setor()
        setor.id = 0
    else:
        setor = Setor.query.filter(Setor.id == id).first()

    if request.method == 'POST':
        form = SetorForm(formdata=request.form)
        form.populate_obj(setor)

        SalvarEntidade(form,setor)
    else:
        form = SetorForm(obj=setor)

    return render_template('editarSetor.html', form=form, auditoria = logsAuditoria(setor))


@setores.route('/remover/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Remover(id):
    setor = Setor.query.filter(Setor.id == id).first()
    RemoverEntidade(setor)
    return redirect(url_for('.Listar'))
