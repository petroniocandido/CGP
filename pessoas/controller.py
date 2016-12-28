#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms_alchemy import ModelForm, ModelFormField, ModelFieldList
from wtforms import StringField, HiddenField, SelectField, FormField, BooleanField, FieldList, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Optional

from ControllerBase import SalvarEntidade,RemoverEntidade

from DomainModel import Pessoa, EstadoCivil, TipoServidor, SituacaoServidor, \
    UF, JornadaTrabalho, Sexo, TipoSanguineo, TipoContaBancaria, Telefone, Endereco, Cargo, Titulo, Titulacao, Perfil

pessoas = Blueprint('pessoas', __name__)


class PessoaBuscaForm(Form):
    id = HiddenField('id')
    nome = StringField('Nome')


class TelefoneForm(ModelForm):
    class Meta:
        model = Telefone


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        include = ['id']

    telefone1 = ModelFormField(TelefoneForm)
    telefone2 = ModelFormField(TelefoneForm)
    endereco = ModelFormField(EnderecoForm)
    cargo_id = SelectField('Cargo', coerce=int, choices=[(c.id, c.nome) for c in Cargo.query.order_by('nome')])
    perfil_id = SelectField('Perfil', coerce=int, choices=[(c.id, c.nome) for c in Perfil.query.order_by('nome')])
    dataNascimento = DateField("Posse", format="%Y-%m-%d", validators=[Optional()])
    dataPosse = DateField("Posse", format="%Y-%m-%d", validators=[Optional()])
    dataExercicio = DateField("Exercício", format="%Y-%m-%d", validators=[Optional()])
    dataSaida = DateField("Saída", format="%Y-%m-%d", validators=[Optional()])
    senha = PasswordField()


@pessoas.route('/listar/', methods=('GET', 'POST'))
def Listar():
    pessoa = Pessoa()
    if request.method == 'GET':
        pessoas = Pessoa.query.order_by(Pessoa.nome).all()
        form = PessoaBuscaForm(obj=pessoa)
    else:
        form = PessoaBuscaForm(formdata=request.form)
        form.populate_obj(pessoa)
        pessoas = Pessoa.query.filter(Pessoa.nome.match(pessoa.nome + "*")).all()

    return render_template('listarPessoas.html', form=form, listagem=pessoas, TS=TipoServidor.__members__)


@pessoas.route('/editar/<int:id>', methods=('GET', 'POST'))
def Editar(id=0):
    if id == 0:
        pessoa = Pessoa()
        pessoa.id = 0
    else:
        pessoa = Pessoa.query.filter(Pessoa.id == id).first()

    if request.method == 'POST':
        form = PessoaForm(formdata=request.form)
        form.populate_obj(pessoa)
        if form.senha.data is not None:
            pessoa.set_senha(form.senha.data)

            SalvarEntidade(form,pessoa)
    else:
        form = PessoaForm(obj=pessoa)

    return render_template('editarPessoa.html', form=form, titulos=pessoa.titulos, TIT=Titulacao.__members__)


@pessoas.route('/remover/<int:id>', methods=('GET', 'POST'))
def Remover(id):
    pessoa = Pessoa.query.filter(Pessoa.id == id).first()
    RemoverEntidade(pessoa)
    return redirect(url_for('.Listar'))
