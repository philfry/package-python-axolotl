%global pname axolotl

Name: python-%{pname}
Version: 0.2.3
Release: 2%{?dist}
Summary: python port of libaxolotl-android
License: GPLv3+
URL: https://github.com/tgalal/%{name}
Source: https://github.com/tgalal/%{name}/archive/%{version}.tar.gz
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This is a ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging environments.


%if 0%{?fedora} && 0%{?fedora} <= 31
%package -n python2-%{pname}
Summary: python port of libaxolotl-android
Requires: protobuf-python >= 2.6.0
Requires: %{name}
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: protobuf-python >= 2.6.0
BuildRequires: python2-crypto >= 2.6.0
BuildRequires: python2-axolotl-curve25519

%description -n python2-%{pname}
This is a ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging environments.
Python 2 version.
%endif


%package -n python3-%{pname}
Summary: python port of libaxolotl-android
Requires: python3-protobuf >= 3.2.0
Requires: %{name}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-protobuf >= 3.2.0
BuildRequires: python3-crypto >= 2.6.0
BuildRequires: python3-axolotl-curve25519

%description -n python3-%{pname}
This is a ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging environments.
Python 3 version.


%prep
%setup -q


%build
%if 0%{?fedora} && 0%{?fedora} <= 31
%py2_build
%endif
%py3_build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
%if 0%{?fedora} && 0%{?fedora} <= 31
%py2_install
%endif
%py3_install


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE


%if 0%{?fedora} && 0%{?fedora} <= 31
%files -n python2-%{pname}
%{python2_sitelib}/%{pname}/
%{python2_sitelib}/*.egg-info/
%endif


%files -n python3-%{pname}
%{python3_sitelib}/%{pname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Sat May  2 2020 Philippe Kueck <projects@unixadm.org> - 0.2.3-2
- prepare for Fedora 32

* Tue Nov  5 2019 Philippe Kueck <projects@unixadm.org> - 0.2.3-1
- new upstream version

* Thu Apr 12 2018 Philippe Kueck <projects@unixadm.org> - 0.1.42-1
- new upstream version

* Fri Mar  9 2018 Philippe Kueck <projects@unixadm.org> - 0.1.39-1
- add python3 packages
