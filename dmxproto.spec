#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dmxproto
Version  : 2.3.1
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/proto/dmxproto-2.3.1.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/dmxproto-2.3.1.tar.bz2
Summary  : DMX extension headers
Group    : Development/Tools
License  : MIT
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
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


%package dev32
Summary: dev32 components for the dmxproto package.
Group: Default

%description dev32
dev32 components for the dmxproto package.


%prep
%setup -q -n dmxproto-2.3.1
pushd ..
cp -a dmxproto-2.3.1 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/dmx.h
/usr/include/X11/extensions/dmxproto.h
/usr/lib64/pkgconfig/dmxproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32dmxproto.pc
