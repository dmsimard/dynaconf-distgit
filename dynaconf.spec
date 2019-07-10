%global srcname dynaconf
%global common_desc \
Dynaconf is a layered configuration system for Python applications with strong \
support for 12-factor applications and extensions for Flask and Django

Name:           %{srcname}
Version:        2.0.3
Release:        1%{?dist}
Summary:        Dynaconf is a dynamic configurator for python projects

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        %{pypi_source}

BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-box
BuildRequires:  python3-click
BuildRequires:  python3-dotenv
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-toml

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{_bindir}/%{srcname}

%changelog
* Fri Jul 5 2019 David Moreau Simard <dmsimard@redhat.com> - 2.0.3-1
- First version of the package
