%define 	module	alabaster
Summary:	A configurable sidebar-enabled Sphinx theme
Summary(pl.UTF-8):	Konfigurowany motyw z bocznym panelem dla Sphinksa
Name:		python3-%{module}
Version:	1.0.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/alabaster/
Source0:	https://pypi.debian.net/alabaster/%{module}-%{version}.tar.gz
# Source0-md5:	c6c2173e5565fb12f08bef410ea50f72
URL:		https://pypi.org/project/alabaster/
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A configurable sidebar-enabled Sphinx theme.

This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his Requests project), which was itself
originally based on @mitsuhiko's theme used for Flask & related
projects.

%description -l pl.UTF-8
Konfigurowany motyw z bocznym panelem (sidebarem) dla Sphinksa.

Motyw ten to zmodyfikowany motyw Sphinksa "Kr" od @kennethreitz
(konkretnie wersja używana w jego projekcie Requests), pierwotnie
oparty na motywie @mitsuhiko używanym w projekcie Flash i powiązanych
z nim.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
