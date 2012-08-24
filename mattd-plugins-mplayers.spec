%global modname mattd.plugins.mplayer

Name:           mattd-plugins-mplayer
Version:        0.0.1
Release:        1%{?dist}
Summary:        MPlayer plugin for Matt Daemon
Group:          Applications/Internet
License:        AGPLv3+
URL:            http://mattd.rtfd.org/
Source0:        http://pypi.python.org/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  mattd

Requires:       mattd
Requires:       espeak
Requires:       mplayer
Requires:       python-sh

%description
MPlayer plugin for Matt Daemon.  Rock James Brown on command!

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%files
%doc README.rst LICENSE

%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py*.egg-info/

%changelog
* Fri Aug 24 2012 Ralph Bean <rbean@redhat.com> - 0.0.1-1
- Initial packaging.
