Summary:     mpack and munpack MIME e-mail utilities
Summary(pl): mpack i munpack - narzêdzia do MIME w poczcie elektronicznej
Name:        mpack
Version:     1.5
Release:     4
Copyright:   Distributable
Group:       Utilities/Mail
Source:      ftp://ftp.andrew.cmu.edu/pub/mpack/%{name}-%{version}-src.tar.Z
Patch:       mpack-tmp.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
Mpack and munpack are utilities for encoding and decoding (respectively)
binary files in MIME (Multipurpose Internet Mail Extensions) format mail
messages. For compatibility with older forms of transferring binary files,
the munpack program can also decode messages in split-uuencoded format.
The Macintosh version can also decode messages in split-BinHex format.

%description -l pl
Programy mpack i munpack s³u¿± do kodowania i dekodowania (rekursywnie)
plików binarnych w formacie MIME (Multipurpose Internet Mail Extensions)
poczty elektronicznej. Dla zachowania kompatybilno¶ci program munpack tak¿e
potrafi dekodowaæ listy w foemacie split-uuencoded.

%prep
%setup -q -n mpack
%patch -p1

%build
rm -rf $RPM_BUILD_ROOT
make CC="gcc" OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
install -s {mpack,munpack} $RPM_BUILD_ROOT/usr/bin
install unixpk.man $RPM_BUILD_ROOT/usr/man/man1/mpack.1
install unixunpk.man $RPM_BUILD_ROOT/usr/man/man1/munpack.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644, root, root, 755)
%doc README.unix
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5-4]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- fiew simplification in %build, %istall and %files,
- added full %attr description in %files.

* Tue Apr 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Build for RH5

* Sun Mar 22 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Build Root'ed
- Moved to /usr/bin
- Added %attr in %install
- Added %clean
