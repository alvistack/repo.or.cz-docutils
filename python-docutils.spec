# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-docutils
Epoch: 100
Version: 0.20.1
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
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
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
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
%{python3_sitelib}/*
%endif

%changelog
