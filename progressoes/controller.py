#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms_alchemy import ModelForm, ModelFormField, ModelFieldList
from wtforms import StringField, HiddenField, SelectField, FormField, BooleanField, FieldList
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Optional

from ControllerBase import SalvarEntidade, RemoverEntidade
from DomainModel import Pessoa, Progressao, ClasseNivel

progressoes = Blueprint('progressoes', __name__)


class ProgressaoForm(ModelForm):
    class Meta:
        model = Progressao
        include = ['id', 'pessoa_id']

    classenivel_id = SelectField('Classe/Nível', coerce=int, \
                                 choices=[(c.id, c) for c in ClasseNivel.query.order_by('id')])


@progressoes.route('/editar/<int:pessoa_id>,<int:progressao_id>', methods=('GET', 'POST'))
def Editar(pessoa_id=0, progressao_id=0):
    if progressao_id == 0:
        progressao = Progressao()
        progressao.id = 0
        progressao.pessoa_id = pessoa_id
    else:
        progressao = Progressao.query.filter(Progressao.id == progressao_id).first()

    if request.method == 'POST':
        form = ProgressaoForm(formdata=request.form)
        form.populate_obj(progressao)
        SalvarEntidade(form,progressao)
    else:
        form = ProgressaoForm(obj=progressao)

    return render_template('editarProgressao.html', form=form)


@progressoes.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    progressao = Progressao.query.filter(Progressao.id == id).first()
    pessoa_id = progressao.pessoa_id
    RemoverEntidade(progressao)
    return redirect(url_for('pessoas.Editar', id=pessoa_id))
