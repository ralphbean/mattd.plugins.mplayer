%global modname mattd.plugins.mplayer

Name:           mattd-plugins-mplayer
Version:        0.0.6
Release:        1%{?dist}
Summary:        MPlayer plugin for Matt Daemon
Group:          Applications/Internet
License:        AGPLv3+
URL:            http://mattd.rtfd.org/
Source0:        http://pypi.python.org/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  mattd

Requires:       mattd
Requires:       espeak
Requires:       mplayer
Requires:       python-sh

%description
MPlayer plugin for Matt Daemon.  Declare victory and play your theme song!

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/mattd/mplayer
%{__cp} data/trololo.ogg  %{buildroot}%{_datadir}/mattd/mplayer/.
%{__mkdir_p} %{buildroot}%{_sysconfdir}/mattd.d
%{__cp} production.ini %{buildroot}%{_sysconfdir}/mattd.d/mplayer.ini

%files
%doc README.rst LICENSE

%config(noreplace) %{_sysconfdir}/mattd.d/mplayer.ini
%{_datadir}/mattd/mplayer/trololo.ogg

%{python_sitelib}/mattd/plugins/mplayer
%{python_sitelib}/%{modname}-%{version}-py*.egg-info/
%{python_sitelib}/%{modname}-%{version}-py*.pth

%changelog
* Fri Aug 24 2012 Ralph Bean <rbean@redhat.com> - 0.0.6-1
- Initial packaging.
