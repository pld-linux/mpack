Summary:	mpack and munpack MIME e-mail utilities
Summary(pl):	mpack i munpack - narz�dzia MIME do poczty elektronicznej
Name:		mpack
Version:	1.5
Release:	5
Copyright:	Distributable
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source:		ftp://ftp.andrew.cmu.edu/pub/mpack/%{name}-%{version}-src.tar.Z
Patch:		mpack-tmp.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Mpack and munpack are utilities for encoding and decoding (respectively)
binary files in MIME (Multipurpose Internet Mail Extensions) format mail
messages. For compatibility with older forms of transferring binary files,
the munpack program can also decode messages in split-uuencoded format.
The Macintosh version can also decode messages in split-BinHex format.

%description -l pl
Programy mpack i munpack s�u�� do kodowania i dekodowania (rekursywnie)
plik�w binarnych w formacie MIME (Multipurpose Internet Mail Extensions)
poczty elektronicznej. Dla zachowania kompatybilno�ci program munpack tak�e
potrafi dekodowa� listy w foemacie split-uuencoded.

%prep
%setup -q -n mpack
%patch -p1

%build
make CC="gcc" OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -s {mpack,munpack} $RPM_BUILD_ROOT%{_bindir}
install unixpk.man $RPM_BUILD_ROOT%{_mandir}/man1/mpack.1
install unixunpk.man $RPM_BUILD_ROOT%{_mandir}/man1/munpack.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README.unix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.unix.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
