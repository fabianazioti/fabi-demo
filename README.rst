# fabi-demo

Publicação Automática no TestPyPI, PyPI e GitHub Release
--------------------------------------------------------


Este repositório utiliza GitHub Actions para automatizar a geração de versões, build do pacote, publicação no TestPyPI, publicação no PyPI e criação de Releases no GitHub e pré-releases.

O workflow suporta:

- Publicações normais (ex.: v1.0.0)
- Pré-releases (ex.: v1.0.0a1, v1.0.0b1, v1.0.0rc1)
- Atualização automática do pyproject.toml
- Upload de artifacts
- Criação automática do GitHub Release com release notes geradas pelo GitHub
- Pré-releases vão apenas para TestPyPI
- Releases finais vão para TestPyPI e PyPI
- A Release no GitHub só é criada se o upload correspondente for bem-sucedido

Como publicar uma versão
++++++++++++++++++++++++

A publicação é feita exclusivamente através da criação de uma tag no GitHub.

Padrões aceitos de tag:

Versão final::

    v1.2.3

Pré-release::

    v1.2.3a1
    v1.2.3b1
    v1.2.3rc1


Requisitos de Autenticação
++++++++++++++++++++++++++

GitHub Actions Secrets::

    Settings → Secrets and variables → Actions → New repository secret

Secrets::

    TEST_PYPI_API_TOKEN	Publicação de pré-release e testes
    PYPI_API_TOKEN	Publicação de releases finais
    GITHUB_TOKEN	Automático (não precisa criar)

Permissões do GitHub Actions::

    Settings → Actions → General
    Workflow permissions → Read and Write

Sem estas permissões, o Actions não conseguirá criar releases nem fazer commits.


