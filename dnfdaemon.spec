Summary:	DBus daemon for doing package action with the dnf package manager
Name:		dnfdaemon
Version:	0.3.19
Release:	2
License:	GPLv2+
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdaemon
Source0:	https://github.com/manatools/dnfdaemon/releases/download/dnfdaemon-%{version}/dnfdaemon-%{version}.tar.xz
Patch0:		https://src.fedoraproject.org/rpms/dnfdaemon/raw/master/f/0001-Enforce-usage-of-versioned-Python-interpreter-in-Mak.patch
Patch1:		https://src.fedoraproject.org/rpms/dnfdaemon/raw/master/f/0002-Handle-removal-of-dnf.repo._md_expire_cache-in-DNF-3.patch
Patch2:		https://src.fedoraproject.org/rpms/dnfdaemon/raw/master/f/0003-Handle-additional-DNF-transaction-callback-actions-i.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
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

# Death to Python 2!
rm -rf %{buildroot}%{py2_puresitedir}

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
