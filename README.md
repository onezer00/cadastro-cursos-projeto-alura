# Projeto para a disciplina de Programação Orientada a Objetos

- Este projeto é um curso online de programação online.
- O objetivo é aprender a programar em Python utilizando Django.
- Além disso, o projeto tem como objetivo aprender a utilizar o framework Django.
- O projeto foi desenvolvido por [@alura](https://www.alura.com.br)
- O projeto está disponível no [GitHub](https://github.com/onezer00/cadastro-cursos-projeto-alura)
- O serviço está rodando no [Heroku](https://cadastro-cursos.herokuapp.com/)
---
<p align="center">
<img src="https://img.shields.io/github/issues/onezer00/cadastro-cursos-projeto-alura?style=plastic" />
<img src="https://img.shields.io/github/forks/onezer00/cadastro-cursos-projeto-alura?style=plastic" />
<img src="https://img.shields.io/github/stars/onezer00/cadastro-cursos-projeto-alura?style=plastic" />
<img src="https://img.shields.io/github/license/onezer00/cadastro-cursos-projeto-alura" />
</p>
Esse projeto foi desenvolvido com o intuíto de a partir do curso de programação online de Python do [Alura](https://www.alura.com.br), disponibilizar uma API pública que a comunidade possa utilizar.

# Alguns detalhes sobre o projeto
- Apesar da API ser pública, é necessário autenticação para acessar os dados.
Caso você precise de uma autenticação, favor entrar em contato através deste [e-mail](mailto:caimbebr@gmail.com) (Este método poderá demorar um pouco mais do que o normal).
- Ou caso prefira, abra uma Issue em [GitHub](https://github.com/onezer00/cadastro-cursos-projeto-alura/issues), para que eu possa te ajudar.
- Estou trabalhando para melhorar o sistema de autenticação, por favor, aguarde.

# Endpoints

A documentação completa da API está disponível [aqui](https://cadastro-cursos.herokuapp.com/docs).

- ``/api/cursos``: Lista todos os cursos cadastrados.
- ``/api/curso/{id}``: Retorna um curso específico.
- ``/api/curso/{id}/matriculas``: Retorna todas as inscrições de um curso.
- ``/api/alunos``: Lista todos os alunos cadastrados.
- ``/api/aluno/{id}``: Retorna um aluno específico.
- ``/api/aluno/{id}/matriculas``: Retorna todas as inscrições de um aluno.
- ``/api/matriculas``: Lista todas as matriculas cadastradas.
