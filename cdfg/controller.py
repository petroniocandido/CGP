#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from ControllerBase import SalvarEntidade, RemoverEntidade, logsAuditoria

from DomainModel import CargoFuncaoGratificada, ClasseCargoFuncao

cdfg = Blueprint('cdfg', __name__)


class CargoFuncaoGratificadaForm(ModelForm):
    class Meta:
        model = CargoFuncaoGratificada
        include = ['id']


@cdfg.route('/listar/')
def Listar():
    cdfg = CargoFuncaoGratificada.query.all()
    return render_template('listarCdfg.html', listagem=cdfg, CL=ClasseCargoFuncao.__members__)


@cdfg.route('/editar/<int:id>', methods=('GET', 'POST'))
def Editar(id=0):
    if id == 0:
        cdfg = CargoFuncaoGratificada()
        cdfg.id = 0
    else:
        cdfg = CargoFuncaoGratificada.query.filter(CargoFuncaoGratificada.id == id).first()

    if request.method == 'POST':
        form = CargoFuncaoGratificadaForm(formdata=request.form)
        form.populate_obj(cdfg)
        SalvarEntidade(form, cdfg)

    else:
        form = CargoFuncaoGratificadaForm(obj=cdfg)

    return render_template('editarCdfg.html', form=form, auditoria = logsAuditoria(cdfg))


@cdfg.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    cdfg = CargoFuncaoGratificada.query.filter(CargoFuncaoGratificada.id == id).first()
    RemoverEntidade(cdfg)
    return redirect(url_for('.Listar'))