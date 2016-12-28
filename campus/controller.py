#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from ControllerBase import SalvarEntidade, RemoverEntidade, logsAuditoria, requer_autenticacao, requer_autenticacao_autorizacao

from DomainModel import Campus

campus = Blueprint('campus', __name__)


class CampusForm(ModelForm):
    class Meta:
        model = Campus
        include = ['id']


@campus.route('/listar/')
@requer_autenticacao_autorizacao
def Listar():
    campi = Campus.query.all()
    return render_template('listarCampus.html', listagem=campi)


@campus.route('/editar/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Editar(id=0):
    if id == 0:
        campus = Campus()
        campus.id = 0
    else:
        campus = Campus.query.filter(Campus.id == id).first()

    if request.method == 'POST':
        form = CampusForm(formdata=request.form)

        SalvarEntidade(form,campus)
    else:
        form = CampusForm(obj=campus)

    return render_template('editarCampus.html', form=form, auditoria = logsAuditoria(campus))


@campus.route('/remover/<int:id>', methods=('GET', 'POST'))
@requer_autenticacao_autorizacao
def Remover(id):
    campus = Campus.query.filter(Campus.id == id).first()
    RemoverEntidade(campus)
    return redirect(url_for('.Listar'))