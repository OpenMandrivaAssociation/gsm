%define	srcver	1.0-pl10

%define	major	1
%define libname	%mklibname %{name} %{major}

Summary:	Shared libraries for GSM speech compressor
Name:		gsm
Version:	1.0.10
Release:	%mkrel 13
Group:		System/Libraries
License:	distributable
URL:		http://kbs.cs.tu-berlin.de/~jutta/toast.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:         gsm-1.0.10-dyn.patch
Patch1:         gsm-1.0-pl10-includes.patch
Patch2:         gsm-1.0-pl10-utimes.patch
Patch3:         gsm-1.0-pl10-shared.diff
Patch4:         gsm-1.0-pl10-add-includefile.patch  
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%package -n	%{libname}-devel
Summary:	Development libraries for a GSM speech compressor
Group:		Development/C
Obsoletes:	%{name}-devel libgsm-devel
Provides:	%{name}-devel libgsm-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
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

%prep

%setup -q -n %{name}-%{srcver}
%patch0 -p1
%patch1 -p1 -b .includes
%patch2 -p1 -b .utimes
%patch3 -p0 -b .shared
%patch4 -p0 -b .add_h_file

%build

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

ln -snf toast %{buildroot}%{_bindir}/untoast
ln -snf toast %{buildroot}%{_bindir}/tcat

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT ChangeLog* README
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/gsm
%{_mandir}/man3/*


