#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash,redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import Perfil, Permissao, Salvar, Remover

perfis = Blueprint('perfis', __name__)


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        include = ['id']
    permissao_id = SelectField('Permissao', coerce=int, choices=[(c.id, c.url) for c in Permissao.query.order_by('url')])


@perfis.route('/listar/')
def perfisListar():
    perfis = Perfil.query.all()
    return render_template('listarPerfis.html', listagem=perfis)


@perfis.route('/editar/<int:id>', methods=('GET', 'POST'))
@perfis.route('/editar/<int:id>,<string:tab>', methods=('GET', 'POST'))
def perfilEditar(id=0,tab="geral"):
    if id == 0:
        perfil = Perfil()
        perfil.id = 0
    else:
        perfil = Perfil.query.filter(Perfil.id == id).first()

    if request.method == 'POST':
        form = PerfilForm(formdata=request.form)

        if form.validate():
            form.populate_obj(perfil)
            if Salvar(perfil):
                flash('Salvo com sucesso!', 'success')
            else:
                flash('Falha ao salvar!', 'danger')
    else:
        form = PerfilForm(obj=perfil)

    return render_template('editarPerfil.html', tab=tab, form=form, permissoes=perfil.permissoes)


@perfis.route('/remover/<int:id>', methods=('GET', 'POST'))
def perfilRemover(id):
    perfil = Perfil.query.filter(Perfil.id == id).first()
    if Remover(perfil):
        flash('Removido com sucesso!', 'success')
    else:
        flash('Falha ao remover!', 'danger')
    perfis = perfil.query.all()
    return render_template('listarPerfis.html', listagem=perfis)


@perfis.route('/addPermissao/<int:id>,<int:perm>', methods=('GET','POST'))
def perfilAddPermissao(id=0,perm=0):
    perfil = Perfil.query.get_or_404(id)
    permissao = Permissao.query.get_or_404(perm)

    perfil.permissoes.append(permissao)

    if Salvar(perfil):
        flash('Adicionado com sucesso!', 'success')
    else:
        flash('Falha ao adicionar!', 'danger')

    return redirect(url_for('.perfilEditar', id=id, tab="permissoes"))


@perfis.route('/removePermissao/<int:id>,<int:perm>', methods=('GET','POST'))
def perfilRemovePermissao(id=0,perm=0):
    perfil = Perfil.query.get_or_404(id)
    permissao = Permissao.query.get_or_404(perm)

    perfil.permissoes.remove(permissao)

    if Salvar(perfil):
        flash('Removido com sucesso!', 'success')
    else:
        flash('Falha ao remover!', 'danger')

    return redirect(url_for('.perfilEditar', id=id, tab="permissoes"))