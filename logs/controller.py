#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash,redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import Log, Salvar, Remover

logs = Blueprint('logs', __name__)


class LogForm(ModelForm):
    class Meta:
        model = Log
        include = ['id']
    

@logs.route('/listar/')
def logsListar():
    logs = Log.query.order_by(Log.data).all()
    return render_template('listarLogs.html', listagem=logs)


@logs.route('/editar/<int:id>', methods=('GET', 'POST'))
def logEditar(id=0,tab="geral"):
    if id == 0:
        log = Log()
        log.id = 0
    else:
        log = Log.query.filter(Log.id == id).first()

    if request.method == 'POST':
        form = LogForm(formdata=request.form)

        if form.validate():
            form.populate_obj(log)
            if Salvar(log):
                flash('Salvo com sucesso!', 'success')
            else:
                flash('Falha ao salvar!', 'danger')
    else:
        form = LogForm(obj=log)

    return render_template('editarLog.html', tab=tab, form=form)


@logs.route('/remover/<int:id>', methods=('GET', 'POST'))
def logRemover(id):
    log = Log.query.filter(Log.id == id).first()
    if Remover(log):
        flash('Removido com sucesso!', 'success')
    else:
        flash('Falha ao remover!', 'danger')
    logs = log.query.all()
    return render_template('listarLogs.html', listagem=logs)

