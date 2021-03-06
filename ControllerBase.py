#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import flash,session, redirect, url_for, request
from functools import wraps
from CGP.DomainModel import db, Log, appendLog, TipoLog, Salvar, Remover, Pessoa
from CGP.app import app


def requer_autenticacao(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario_id" not in session or session["usuario_id"] is None:
            app.logger.warning("Usuário não autenticado")
            return redirect('login/login')
        session["ultima_url"] = request.path
        return f(*args, **kwargs)
    return decorated


def requer_autenticacao_autorizacao(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario_id" not in session or session["usuario_id"] is None:
            app.logger.warning("Usuário não autenticado")
            return redirect('login/login')
        tmppath = request.path[:request.path.rindex('/')+1]
        if tmppath not in usuarioPermissoes():
            app.logger.warning("Usuário não autorizado")
            flash('Acesso não autorizado!','danger')
            return redirect(session["ultima_url"])
        session["ultima_url"] = request.path
        return f(*args, **kwargs)
    return decorated


def usuarioLogado():
    if session["usuario_id"] is not None:
        return Pessoa.query.filter(Pessoa.id == int(session["usuario_id"])).first()
    else:
        return None


def usuarioPermissoes():
    permissoes = [k.url for k in usuarioLogado().perfil.permissoes]
    return permissoes


def checarPermissaoUsuario(url):
    return url in usuarioPermissoes()

def SalvarEntidadeSimples(obj, mensagem):
    if Salvar(obj):
        appendLog(TipoLog.SUCESSO, mensagem + " realizada", obj)
        flash('Salvo com sucesso!', 'success')
    else:
        appendLog(TipoLog.ERROGRAVE, mensagem + " não realizada!", obj)
        flash('Falha ao salvar!', 'danger')


def RemoverEntidadeSimples(obj, mensagem):
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


def logsAuditoria(obj):
    logs = Log.query.filter(Log.entidade == type(obj).__name__ and  Log.entidade_id == obj.id)\
        .order_by(Log.data.desc()).limit(30)
    return logs
