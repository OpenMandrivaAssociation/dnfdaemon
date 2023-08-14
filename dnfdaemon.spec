Summary:	DBus daemon for doing package action with the dnf package manager
Name:		dnfdaemon
Version:	0.3.22
Release:	1
License:	GPLv2+
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdaemon
Source0:	https://github.com/manatools/dnfdaemon/releases/download/dnfdaemon-%{version}/dnfdaemon-%{version}.tar.xz
#Patch0:		dnfdaemon-0.3.20-python-3.10+.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	make
BuildRequires:	systemd-rpm-macros
Requires:	python-%{name} = %{EVRD}

%description
DBus daemon for doing package action with the dnf package manager

%package -n python-%{name}
Summary:	Python 3 API for communicating with %{name}

%description -n python-%{name}
Python 3 API for communicating with %{name}

%prep
%autosetup -p1

%build

%install
%make_install DATADIR=%{_datadir} SYSCONFDIR=%{_sysconfdir}

%files
%doc README.md ChangeLog
%license COPYING
%{_datadir}/dbus-1/system-services/*
%{_datadir}/dbus-1/services/*
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service
%{_datadir}/polkit-1/actions/*
# this should not be edited by the user, so no %%config
%{_sysconfdir}/dbus-1/system.d/*
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/__init__.py
%{python_sitelib}/%{name}/server

%files -n python-%{name}
%{python_sitelib}/%{name}/client
