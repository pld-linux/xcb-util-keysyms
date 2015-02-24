Summary:	XCB util-keysyms module
Summary(pl.UTF-8):	Moduł XCB util-keysyms
Name:		xcb-util-keysyms
Version:	0.4.0
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	1022293083eec9e62d5659261c29e367
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 1.6
BuildRequires:	xorg-proto-xproto-devel >= 7.0.8
Requires:	libxcb >= 1.4
Conflicts:	xcb-util < 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-keysyms module provides the following library:
- keysyms: Standard X key constants and conversion to/from keycodes.

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util-keysyms udostępnia następującą biliotekę:
- keysyms: standardowe stałe i konwersje klawiszy X z/do kodów
klawiszy.

%package devel
Summary:	Header files for XCB util-keysyms library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-keysyms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4
Conflicts:	xcb-util-devel < 0.3.8

%description devel
Header files for XCB util-keysyms library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util-keysyms.

%package static
Summary:	Static XCB util-keysyms library
Summary(pl.UTF-8):	Statyczna biblioteka XCB util-keysyms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-keysyms library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB util-keysyms.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxcb-keysyms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-keysyms.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-keysyms.so
%{_libdir}/libxcb-keysyms.la
%{_includedir}/xcb/xcb_keysyms.h
%{_pkgconfigdir}/xcb-keysyms.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-keysyms.a
