# gsm is used by libsndfile, libsndfile is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define srcver %(echo %{version} |cut -d. -f1-2)-pl%(echo %{version} |cut -d. -f3-)

%global ver_major 1
%global ver_minor 0
%global ver_patch 19

%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define lib32name %mklib32name %{name} %{major}
%define dev32name %mklib32name %{name} -d

Summary:	Shared libraries for GSM speech compressor
Name:		gsm
Version:	1.0.19
Release:	3
Group:		System/Libraries
License:	Distributable
Url:		https://www.quut.com/gsm/
Source0:	http://www.quut.com/gsm/%{name}-%{version}.tar.gz
Patch0:         %{name}-makefile.patch
Patch1:         %{name}-warnings.patch

%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%files
%doc COPYRIGHT ChangeLog* README
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for GSM speech compressor
Group:		System/Libraries

%description -n %{libname}
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%files -n %{libname}
%{_libdir}/libgsm.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries for a GSM speech compressor
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Contains header files and development libraries for libgsm, an
implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%files -n %{devname}
%{_libdir}/libgsm.so
%{_includedir}/gsm
%{_includedir}/gsm.h
%{_mandir}/man3/*

#----------------------------------------------------------------------------

%if %{with compat32}
%package -n %{lib32name}
Summary:	Shared libraries for GSM speech compressor (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%files -n %{lib32name}
%{_prefix}/lib/libgsm.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{dev32name}
Summary:	Development libraries for a GSM speech compressor (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Contains header files and development libraries for libgsm, an
implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%files -n %{dev32name}
%{_prefix}/lib/libgsm.so
%endif

%prep
%autosetup -p1 -n %{name}-%{srcver}

%build
%if %{with compat32}
mkdir build32
cp -a $(ls -1 |grep -v build32) build32/
cd build32
sed -i -e "s,\$(RPM_OPT_FLAGS),$(echo %{optflags} |sed -e 's,-m64,,g;s,-mx32,,g'),g" Makefile
sed -i -e 's|gcc|gcc -m32|g' Makefile
sed -i -e "s|^LD.*|LD=gcc -m32 $(echo %{optflags} %{ldflags}|sed -e 's,-m64,,g;s,-mx32,,g')|g" Makefile
%make_build all SO_MAJOR=%{ver_major} SO_MINOR=%{ver_minor} SO_PATCH=%{ver_patch} CC="gcc -m32" CXX="g++ -m32" LD="gcc -m32" LDFLAGS="$(echo %{ldflags}|sed -e 's,-m64,,g;s,-mx32,,g') -m32"
cd ..
%endif

sed -i -e 's|gcc -ansi -pedantic|%{__cc} -ansi -pedantic|g' Makefile
sed -i -e 's|^LD.*|LD=%{__cc} %{optflags} %{ldflags}|g' Makefile
export LDFLAGS="%{ldflags}"
%make_build all SO_MAJOR=%{ver_major} SO_MINOR=%{ver_minor} SO_PATCH=%{ver_patch}

%install
mkdir -p %{buildroot}{%{_bindir},%{_includedir}/gsm,%{_libdir},%{_mandir}/{man1,man3}}
%if %{with compat32}
mkdir -p %{buildroot}%{_prefix}/lib
cd build32
export LDFLAGS="%(echo %{ldflags} |sed -e 's,-m64,,g;s,-mx32,,g') -m32"
make install \
	INSTALL_ROOT=%{buildroot}%{_prefix} \
	GSM_INSTALL_INC=%{buildroot}%{_includedir}/gsm \
	GSM_INSTALL_LIB=%{buildroot}%{_prefix}/lib \
	SO_MAJOR=%{ver_major} SO_MINOR=%{ver_minor} SO_PATCH=%{ver_patch}
cd ..
%endif
export LDFLAGS="%{ldflags}"
make install \
	INSTALL_ROOT=%{buildroot}%{_prefix} \
	GSM_INSTALL_INC=%{buildroot}%{_includedir}/gsm \
	GSM_INSTALL_LIB=%{buildroot}%{_libdir} \
	SO_MAJOR=%{ver_major} SO_MINOR=%{ver_minor} SO_PATCH=%{ver_patch}

mkdir -p %{buildroot}%{_bindir}
ln -snf toast %{buildroot}%{_bindir}/untoast
ln -snf toast %{buildroot}%{_bindir}/tcat

ln -s gsm/gsm.h %{buildroot}%{_includedir}

%check
# This is to ensure that the patch creates the proper library version.
[ -f %{buildroot}%{_libdir}/libgsm.so.%{version} ]
export LDFLAGS="%{ldflags}"
make addtst
