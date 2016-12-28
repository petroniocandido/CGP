#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash,redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from ControllerBase import SalvarEntidade, RemoverEntidade
from DomainModel import ClasseNivel, TipoServidor

classenivel = Blueprint('classenivel', __name__)


class ClasseNivelForm(ModelForm):
    class Meta:
        model = ClasseNivel
        include = ['id']


@classenivel.route('/listar/')
def Listar():
    classes = ClasseNivel.query.all()
    return render_template('listarClasseNivel.html', listagem=classes, TS=TipoServidor.__members__)


@classenivel.route('/editar/<int:id>', methods=('GET', 'POST'))
def Editar(id=0):
    if id == 0:
        classenivel = ClasseNivel()
        classenivel.id = 0
    else:
        classenivel = ClasseNivel.query.filter(ClasseNivel.id == id).first()

    if request.method == 'POST':
        form = ClasseNivelForm(formdata=request.form)
        form.populate_obj(classenivel)

        SalvarEntidade(form,classenivel)
    else:
        form = ClasseNivelForm(obj=classenivel)

    return render_template('editarClasseNivel.html', form=form)


@classenivel.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    classenivel = ClasseNivel.query.filter(ClasseNivel.id == id).first()
    RemoverEntidade(classenivel)
    return redirect(url_for('.Listar'))
