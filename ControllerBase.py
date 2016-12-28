#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import db, appendLog, TipoLog, Salvar, Remover


def SalvarEntidade(obj, mensagem):
    if Salvar(obj):
        appendLog(TipoLog.SUCESSO, mensagem + " realizada", obj)
        flash('Salvo com sucesso!', 'success')
    else:
        appendLog(TipoLog.ERROGRAVE, mensagem + " não realizada!", obj)
        flash('Falha ao salvar!', 'danger')


def RemoverEntidade(obj, mensagem):
    if Remover(obj):
        appendLog(TipoLog.SUCESSO, mensagem + " realizada", obj)
        flash('Salvo com sucesso!', 'success')
    else:
        appendLog(TipoLog.ERROGRAVE, mensagem + " não realizada!", obj)
        flash('Falha ao salvar!', 'danger')


def SalvarEntidade(form,obj):
    if form.validate():

        if Salvar(obj):
            appendLog(TipoLog.SUCESSO, "Alteração realizada", obj)
            flash('Salvo com sucesso!', 'success')
        else:
            appendLog(TipoLog.ERROGRAVE, "Alteração não realizada!", obj)
            flash('Falha ao salvar!', 'danger')
    else:
        appendLog(TipoLog.INFO, "Formulário não validadeo, verifique os campos obrigatórios!", obj)
        flash('Falha ao salvar!' + str(form.errors), 'danger')


def RemoverEntidade(obj):
    if Remover(obj):
        appendLog(TipoLog.SUCESSO, "Registro removido com sucesso", obj)
        flash('Removido com sucesso!', 'success')
    else:
        appendLog(TipoLog.ERRO, "Registro não removido!", obj)
        flash('Falha ao remover!', 'danger')