Name:           chromaprint-tools
Version:        0.6
Release:        3%{?dist}
Summary:        Chromaprint audio fingerprinting tools
Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://www.acoustid.org/chromaprint/
Source:         https://github.com/downloads/lalinsky/chromaprint/chromaprint-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3

# examples requires ffmpeg
BuildRequires:  ffmpeg-devel

%description
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

This is a set of Chromaprint tools related to acoustic fingerprinting, 
featuring fpcalc, an standalone AcoustID tool used by Picard.

%prep
%setup -q -n chromaprint-%{version}


%build
%cmake -DBUILD_EXAMPLES=on -DBUILD_TESTS=off
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# cleaning files managed in the chromaprint main package
rm -f %{buildroot}%{_includedir}/chromaprint.h
rm -f %{buildroot}%{_libdir}/pkgconfig/libchromaprint.pc
rm -f %{buildroot}%{_libdir}/lib*.la
rm -f %{buildroot}%{_libdir}/lib*.so*

%files
%doc CHANGES.txt COPYING.txt NEWS.txt README.txt
%{_bindir}/fpcalc

%changelog
* Sat Jan 14 2012 Ismael Olea <ismael@olea.org> - 0.6-3
- using %cmake macro

* Wed Jan 4 2012 Ismael Olea <ismael@olea.org> - 0.6-2
- minor spec cleaning

* Tue Dec 27 2011 Ismael Olea <ismael@olea.org> - 0.6-1
- update to 0.6
- spec cleaning

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.5-2
- first version for RPM-Fusion
- renaming into chromaprint-tools

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- subpackage for fpcalc 

* Sat Aug 06 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4-1
- Initial package
