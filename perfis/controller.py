#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash,redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from ControllerBase import SalvarEntidade,RemoverEntidade, logsAuditoria

from DomainModel import Perfil, Permissao

perfis = Blueprint('perfis', __name__)


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        include = ['id']
    permissao_id = SelectField('Permissao', coerce=int, choices=[(c.id, c.url) for c in Permissao.query.order_by('url')])


@perfis.route('/listar/')
def Listar():
    perfis = Perfil.query.all()
    return render_template('listarPerfis.html', listagem=perfis)


@perfis.route('/editar/<int:id>', methods=('GET', 'POST'))
@perfis.route('/editar/<int:id>,<string:tab>', methods=('GET', 'POST'))
def Editar(id=0,tab="geral"):
    if id == 0:
        perfil = Perfil()
        perfil.id = 0
    else:
        perfil = Perfil.query.filter(Perfil.id == id).first()

    if request.method == 'POST':
        form = PerfilForm(formdata=request.form)

        form.populate_obj(perfil)

        SalvarEntidade(form,perfil)
    else:
        form = PerfilForm(obj=perfil)

    return render_template('editarPerfil.html', tab=tab, form=form, permissoes=perfil.permissoes, auditoria = logsAuditoria(perfil))


@perfis.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    perfil = Perfil.query.filter(Perfil.id == id).first()
    RemoverEntidade(perfil)
    return redirect(url_for('.Listar'))


@perfis.route('/addPermissao/<int:id>,<int:perm>', methods=('GET','POST'))
def perfilAddPermissao(id=0,perm=0):
    perfil = Perfil.query.get_or_404(id)
    permissao = Permissao.query.get_or_404(perm)

    perfil.permissoes.append(permissao)

    SalvarEntidade(perfil,"Adicionar permissão")

    return redirect(url_for('.Editar', id=id, tab="permissoes"))


@perfis.route('/removePermissao/<int:id>,<int:perm>', methods=('GET','POST'))
def perfilRemovePermissao(id=0,perm=0):
    perfil = Perfil.query.get_or_404(id)
    permissao = Permissao.query.get_or_404(perm)

    perfil.permissoes.remove(permissao)

    RemoverEntidade(perfil,"Remover permissão")

    return redirect(url_for('.Editar', id=id, tab="permissoes"))