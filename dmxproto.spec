#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dmxproto
Version  : 2.3.1
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/proto/dmxproto-2.3.1.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/dmxproto-2.3.1.tar.bz2
Summary  : DMX extension headers
Group    : Development/Tools
License  : MIT
BuildRequires : pkgconfig(xorg-macros)

%description
Distributed Multihead X (DMX) Extension
This extension defines a protocol for clients to access a front-end proxy
X server that controls multiple back-end X servers making up a large display.

%package dev
Summary: dev components for the dmxproto package.
Group: Development
Provides: dmxproto-devel

%description dev
dev components for the dmxproto package.


%prep
%setup -q -n dmxproto-2.3.1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/dmx.h
/usr/include/X11/extensions/dmxproto.h
/usr/lib64/pkgconfig/dmxproto.pc
