%global pname axolotl

Name: python-%{pname}
Version: 0.1.39
Release: 2%{?dist}
Summary: python port of libaxolotl-android
Group: Development/Libraries
License: GPLv3+
URL: https://github.com/tgalal/%{name}
Source: https://github.com/tgalal/%{name}/archive/%{version}.tar.gz
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This is a ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging environments.


%package -n python2-%{pname}
Summary: python port of libaxolotl-android
Requires: protobuf-python >= 2.6.0
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: protobuf-python >= 2.6.0
BuildRequires: python2-crypto >= 2.6.0
BuildRequires: python2-axolotl-curve25519

%description -n python2-%{pname}
This is a ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging environments.
Python 2 version.


%package -n python3-%{pname}
Summary: python port of libaxolotl-android
Requires: python3-protobuf >= 3.2.0
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
%py2_build
%py3_build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
%py2_install
%py3_install


%clean
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}


%files -n python2-%{pname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python2_sitelib}/%{pname}/
%{python2_sitelib}/*.egg-info/


%files -n python3-%{pname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python3_sitelib}/%{pname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Fri Mar  9 2018 Philippe Kueck <projects@unixadm.org> - 0.1.39-1
- add python3 packages
