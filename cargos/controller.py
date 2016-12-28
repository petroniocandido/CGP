#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from ControllerBase import SalvarEntidade, RemoverEntidade,logsAuditoria

from DomainModel import Cargo, TipoServidor

cargos = Blueprint('cargos', __name__)


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        include = ['id']


@cargos.route('/listar/')
def Listar():
    cargos = Cargo.query.all()
    return render_template('listarCargos.html', listagem=cargos, TS=TipoServidor.__members__)


@cargos.route('/editar/<int:id>', methods=('GET', 'POST'))
def Editar(id=0):
    if id == 0:
        cargos = Cargo()
        cargos.id = 0
    else:
        cargos = Cargo.query.filter(Cargo.id == id).first()

    if request.method == 'POST':
        form = CargoForm(formdata=request.form)

        form.populate_obj(cargos)

        SalvarEntidade(form, cargos)
    else:
        form = CargoForm(obj=cargos)

    return render_template('editarCargo.html', form=form, auditoria = logsAuditoria(cargos))


@cargos.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    cargos = Cargo.query.filter(Cargo.id == id).first()
    RemoverEntidade(cargos)
    return redirect(url_for('.Listar'))