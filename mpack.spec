Summary:	mpack and munpack MIME e-mail utilities
Summary(pl):	mpack i munpack - narzêdzia MIME do poczty elektronicznej
Name:		mpack
Version:	1.5
Release:	7
License:	distributable
Group:		Applications/Mail
Source0:	ftp://ftp.andrew.cmu.edu/pub/mpack/%{name}-%{version}-src.tar.Z
Patch0:		%{name}-tmp.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpack and munpack are utilities for encoding and decoding
(respectively) binary files in MIME (Multipurpose Internet Mail
Extensions) format mail messages. For compatibility with older forms
of transferring binary files, the munpack program can also decode
messages in split-uuencoded format. The Macintosh version can also
decode messages in split-BinHex format. Using mpack you can easily
send files via mail.

%description -l pl
Programy mpack i munpack s³u¿± do kodowania i dekodowania
(rekursywnie) plików binarnych w formacie MIME (Multipurpose Internet
Mail Extensions) poczty elektronicznej. Dla zachowania kompatybilno¶ci
program munpack tak¿e potrafi dekodowaæ listy w formacie
split-uuencoded. Za pomoc± programu mpack mo¿na ³atwo (z linii
poleceñ) wysy³aæ pliki poczt±.

%prep
%setup -q -n mpack
%patch -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mpack munpack $RPM_BUILD_ROOT%{_bindir}
install unixpk.man $RPM_BUILD_ROOT%{_mandir}/man1/mpack.1
install unixunpk.man $RPM_BUILD_ROOT%{_mandir}/man1/munpack.1

gzip -9nf README.unix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.unix.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
