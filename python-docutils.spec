%global debug_package %{nil}

Name: python-docutils
Epoch: 100
Version: 0.17.1
Release: 1%{?dist}
BuildArch: noarch
Summary: System for processing plaintext documentation
License: BSD-2-Clause
URL: https://pypi.org/project/docutils/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The Docutils project specifies a plaintext markup language,
reStructuredText, which is easy to read and quick to write. The project
includes a python library to parse rST files and transform them into
other useful formats such as HTML, XML, and TeX as well as commandline
tools that give the enduser access to this functionality. Currently, the
library supports parsing rST that is in standalone files and PEPs
(Python Enhancement Proposals). Work is underway to parse rST from
Python inline documentation modules and packages.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-docutils
Summary: System for processing plaintext documentation
Requires: python3
Provides: python3-docutils = %{epoch}:%{version}-%{release}
Provides: python3dist(docutils) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-docutils = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(docutils) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-docutils = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(docutils) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-docutils
The Docutils project specifies a plaintext markup language,
reStructuredText, which is easy to read and quick to write. The project
includes a python library to parse rST files and transform them into
other useful formats such as HTML, XML, and TeX as well as commandline
tools that give the enduser access to this functionality. Currently, the
library supports parsing rST that is in standalone files and PEPs
(Python Enhancement Proposals). Work is underway to parse rST from
Python inline documentation modules and packages.

%files -n python%{python3_version_nodots}-docutils
%license COPYING.txt
%{_bindir}/*
%{python3_sitelib}/docutils*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
%package -n python3-docutils
Summary: System for processing plaintext documentation
Requires: python3
Provides: python3-docutils = %{epoch}:%{version}-%{release}
Provides: python3dist(docutils) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-docutils = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(docutils) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-docutils = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(docutils) = %{epoch}:%{version}-%{release}

%description -n python3-docutils
The Docutils project specifies a plaintext markup language,
reStructuredText, which is easy to read and quick to write. The project
includes a python library to parse rST files and transform them into
other useful formats such as HTML, XML, and TeX as well as commandline
tools that give the enduser access to this functionality. Currently, the
library supports parsing rST that is in standalone files and PEPs
(Python Enhancement Proposals). Work is underway to parse rST from
Python inline documentation modules and packages.

%files -n python3-docutils
%license COPYING.txt
%{_bindir}/*
%{python3_sitelib}/docutils*
%endif

%changelog
