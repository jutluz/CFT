const url = "http://localhost:5000";

// Logout
$(function () {

    $("#logout").on("click", function () {
        if (sessionStorage.getItem("TOKEN") == undefined) {
            alert("Faça login.");
        } else {
            sessionStorage.removeItem("TOKEN");
            alert("Deslogado.")
        }
    })

    // Cadastro
    $("#cadastrar-aluno").on("click", function () {
        let nome = $("#nome-aluno-cadastro").val();
        let email = $("#email-aluno-cadastro").val();
        let senha = $("#senha-aluno-cadastro").val();
        let turma_id = $("#turma-aluno-cadastro").val();

        let dados = {
            nome: nome,
            email: email,
            senha: senha,
            turma_id: turma_id
        }

        $.ajax({
            url: `${url}/cadastro/${this.getAttribute("rel")}`,
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(dados),
            success: (resposta) => {
                if (resposta.resultado == "ok") {
                    sessionStorage.setItem("TOKEN", resposta.detalhes);
                    alert("Cadastrado com sucesso :)");
                } else {
                    alert("Ops! Não deu certo.");
                }
            },
            error: (resposta) => {
                alert(resposta.detalhes);
            }
        });


    });

    // Login
    $("#logar").on("click", function () {
        let email = $("#email").val();
        let senha = $("#senha").val();

        dados = {
            login: email,
            senha: senha
        };

        $.ajax({
            url: `${url}/login`,
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(dados),
            success: (resposta) => {
                if (resposta.resultado == "ok") {
                    sessionStorage.setItem("TOKEN", resposta.detalhes);
                    alert("Logado com sucesso.");
                } else {
                    alert("Verifique se seu e-mail e senha estão corretos.");
                }
            },
            error: (resposta) => {
                alert(resposta.detalhes);
            }
        });
    });

    // Listagem
    $(".listar").on("click", function () {
        $.ajax({
            url: `${url}/listar/${this.text}`,
            method: "GET",
            success: (resposta) => criarTabela(resposta, this.text),
            error: () => alert("Ops! A listagem não funcionou")
        });
    });

    // Adicionar aluno
    $("#enviar-aluno").on("click", function () {
        let nome = $("#nome-aluno").val();
        let email = $("#email-aluno").val();
        let senha = $("#senha-aluno").val();
        let turma_id = $("#turma-aluno").val();

        let dados = {
            nome: nome,
            email: email,
            senha: senha,
            turma_id: turma_id
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    // Adicionar autor
    $("#enviar-autor").on("click", function () {
        let nome = $("#nome-autor").val();

        let dados = {
            nome: nome
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    // Adicionar instrumento
    $("#enviar-instrumento").on("click", function () {
        let nome = $("#nome-instrumento").val();
        let turma_id = $("#turma-instrumento").val();

        let dados = {
            nome: nome,
            turma_id: turma_id
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    $("#enviar-instrumento").on("click", function () {
        let nome = $("#nome-instrumento").val();
        let autor_id = $("#autor-instrumento").val();

        let dados = {
            nome: nome,
            autor_id: autor_id
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    // Adicionar música
    $("#enviar-musica").on("click", function () {
        let nome = $("#nome-musica").val();
        let autor_id = $("#autor-musica").val();

        let dados = {
            nome: nome,
            autor_id: autor_id
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    // Adicionar professor
    $("#enviar-professor").on("click", function () {
        let nome = $("#nome-professor").val();
        let email = $("#email-professor").val();
        let senha = $("#senha-professor").val();
        let turma_id = $("#turma-professor").val();
        let salario = $("#salario-professor").val();

        let dados = {
            nome: nome,
            email: email,
            senha: senha,
            turma_id: turma_id,
            salario
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    // Adicionar turma
    $("#enviar-turma").on("click", function () {
        let semestre = $("#semestre-turma").val();
        let ano = $("#ano-turma").val();
        let agenda_id = $("#agenda-turma").val();

        let dados = {
            semestre: semestre,
            ano: ano,
            agenda_id: agenda_id
        }

        enviarDados(dados, this.getAttribute("rel"));
    });

    // Editar aluno
    $("#editar-aluno").on("click", function () {
        let nome = $("#nome-aluno-editar").val();
        let email = $("#email-aluno-editar").val();
        let senha = $("#senha-aluno-editar").val();
        let turma_id = $("#turma-aluno-editar").val();

        let dados = {
            nome: nome,
            email: email,
            senha: senha,
            turma_id: turma_id
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    // Editar autor
    $("#editar-autor").on("click", function () {
        let nome = $("#nome-autor-editar").val();

        let dados = {
            nome: nome
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    // Editar instrumento
    $("#editar-instrumento").on("click", function () {
        let nome = $("#nome-instrumento-editar").val();
        let turma_id = $("#turma-instrumento-editar").val();

        let dados = {
            nome: nome,
            turma_id: turma_id
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    $("#editar-instrumento").on("click", function () {
        let nome = $("#nome-instrumento-editar").val();
        let autor_id = $("#autor-instrumento-editar").val();

        let dados = {
            nome: nome,
            autor_id: autor_id
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    // Editar música
    $("#editar-musica").on("click", function () {
        let nome = $("#nome-musica-editar").val();
        let autor_id = $("#autor-musica-editar").val();

        let dados = {
            nome: nome,
            autor_id: autor_id
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    // Editar professor
    $("#editar-professor").on("click", function () {
        let nome = $("#nome-professor-editar").val();
        let email = $("#email-professor-editar").val();
        let senha = $("#senha-professor-editar").val();
        let turma_id = $("#turma-professor-editar").val();
        let salario = $("#salario-professor-editar").val();

        let dados = {
            nome: nome,
            email: email,
            senha: senha,
            turma_id: turma_id,
            salario
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    // Editar turma
    $("#editar-turma").on("click", function () {
        let semestre = $("#semestre-turma-editar").val();
        let ano = $("#ano-turma-editar").val();
        let agenda_id = $("#agenda-turma-editar").val();

        let dados = {
            semestre: semestre,
            ano: ano,
            agenda_id: agenda_id
        }

        editarDados(dados, this.getAttribute("rel"), this.getAttribute("editar"));
    });

    // ---------------------- FUNÇÕES ------------------------
    function enviarDados(dados, entidade) {
        if (sessionStorage.getItem("TOKEN") == undefined) {
            alert("Faça login.");
            return;
        }
        $.ajax({
            url: `${url}/adicionar/${entidade}`,
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(dados),
            headers: { Authorization: `Bearer ${sessionStorage.getItem("TOKEN")}` },
            success: (resposta) => {
                alert(resposta.detalhes);
            },
            error: (resposta) => {
                alert(resposta.detalhes);
            }
        });
    }

    function editarDados(dados, entidade, id) {
        if (sessionStorage.getItem("TOKEN") == undefined) {
            alert("Login necessário para esta ação.");
            return;
        }
        $.ajax({
            url: `${url}/editar/${entidade}/${id}`,
            method: "PUT",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(dados),
            headers: { Authorization: `Bearer ${sessionStorage.getItem("TOKEN")}` },
            success: (resposta) => {
                alert(resposta.detalhes);
            },
            error: (resposta) => {
                alert(resposta.detalhes);
            }
        });
    }

    function criarTabela(dados, entidade) {
        console.log(entidade);
        let tabela = criarCabecalho(dados);
        tabela += "<tbody>";
        linha = "";
        for (var i in dados) {
            linha += "<tr>";
            for (var j in dados[i]) {
                if (j == "senha") continue;
                linha += (dados[i][j].nome) ? `<td>${dados[i][j].nome}</td>` : `<td>${dados[i][j]}</td>`;
            }
            linha += `<td><a href="#" onclick="deletar(${dados[i].id}, '${entidade}')">Deletar</a></td>`
            linha += `<td><a href="#" data-bs-toggle="modal" data-bs-target="#${entidade.toLowerCase()}-modal-editar" onclick="editar(${dados[i].id}, '${entidade}')">Editar</a></td>`
            linha += "</tr>";
        }
        tabela += linha + "</tbody></table>";
        $("#a").html(tabela);
    }

    function criarCabecalho(dados) {
        let colunas = "";
        for (var i of Object.keys(dados[0])) {
            if (i == "senha") continue;
            colunas += `<td>${capitalize(i)}</td>`;
        }
        let tabela = `<table class="table">
                            <thead>
                                <tr>
                                    ${colunas}
                                    <td>Remover</td>
                                    <td>Editar</td>
                                </tr>
                            </thead>
                        `;
        return tabela;
    }




});


function deletar(id, entidade) {
    if (sessionStorage.getItem("TOKEN") == undefined) {
        alert("FAZ LOGIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        return;
    }
    $.ajax({
        url: `${url}/remover/${entidade}/${id}`,
        method: "DELETE",
        headers: { Authorization: `Bearer ${sessionStorage.getItem("TOKEN")}` },
        success: (resposta) => {
            alert(resposta.detalhes);
        },
        error: (resposta) => {
            alert(resposta.detalhes);
        }
    });
}

function editar(id, entidade) {
    $(`#editar-${entidade.toLowerCase()}`).attr("editar", id);
}

function capitalize(str) {
    console.log(str);
    return str.charAt(0).toUpperCase() + str.slice(1);
}