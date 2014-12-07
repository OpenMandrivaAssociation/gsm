%define	srcver	1.0-pl13
%define	major	1
%define libname	%mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Shared libraries for GSM speech compressor
Name:		gsm
Version:	1.0.13
Release:	17
Group:		System/Libraries
License:	distributable
Url:		http://www.quut.com/gsm/
Source0:	http://www.quut.com/gsm/%{name}-%{version}.tar.gz
Patch0:         gsm-1.0.10-dyn.patch
Patch1:         gsm-1.0-pl10-includes.patch
Patch3:         gsm-1.0-pl10-shared.diff
Patch4:         gsm-1.0-pl10-add-includefile.patch  

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

%package -n	%{libname}
Summary:	Shared libraries for GSM speech compressor
Group:          System/Libraries

%description -n	%{libname}
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

%package -n	%{devname}
Summary:	Development libraries for a GSM speech compressor
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel

%description -n	%{devname}
Contains header files and development libraries for libgsm, an
implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.

%prep
%setup -qn %{name}-%{srcver}
%apply_patches

%build
sed -i 's|gcc -ansi -pedantic|%{__cc} -ansi -pedantic|g' Makefile
%make

%install
%makeinstall

rm -f %{buildroot}%{_libdir}/*.a
ln -snf toast %{buildroot}%{_bindir}/untoast
ln -snf toast %{buildroot}%{_bindir}/tcat

%files
%doc COPYRIGHT ChangeLog* README
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libgsm.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/gsm
%{_mandir}/man3/*

