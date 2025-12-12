Name:		python-requests-oauthlib
Version:	2.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/requests-oauthlib/requests-oauthlib-%{version}.tar.gz
Summary:	OAuthlib authentication support for Requests.
URL:		https://pypi.org/project/requests-oauthlib/
License:	ISC
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
OAuthlib authentication support for Requests.

%prep
%autosetup -p1 -n requests-oauthlib-%{version}

%files
%{py_sitedir}/requests_oauthlib
%{py_sitedir}/requests_oauthlib-*.*-info
