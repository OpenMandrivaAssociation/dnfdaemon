Summary:	DBus daemon for doing package action with the dnf package manager
Name:		dnfdaemon
Version:	0.3.20
Release:	1
License:	GPLv2+
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdaemon
Source0:	https://github.com/manatools/dnfdaemon/releases/download/dnfdaemon-%{version}/dnfdaemon-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	make
BuildRequires:	systemd-macros
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
mkdir -p %{buildroot}/lib
mv %{buildroot}%{_prefix}/lib/systemd %{buildroot}/lib

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
%dir %{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}/__*
%{py_puresitedir}/%{name}/server

%files -n python-%{name}
%{py_puresitedir}/%{name}/client
