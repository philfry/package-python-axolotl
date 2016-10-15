Name: python-axolotl
Version: 0.1.35
Release: 1%{?dist}
Summary: Python port of libaxolotl-android
Group: Development/Libraries
License: BSD
URL: https://github.com/tgalal/%{name}
Source: https://github.com/tgalal/%{name}/archive/%{version}.tar.gz
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: protobuf-python >= 2.6.0
BuildRequires: python-crypto >= 2.6.0
BuildRequires: python-axolotl-curve25519


%description
This is a ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging environments.


%prep
%setup -q


%build
python setup.py build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES


%clean
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}


%files -f INSTALLED_FILES
%defattr(-,root,root)
%{!?_licensedir:%global license %%doc}
%license LICENSE
