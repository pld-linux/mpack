Summary:	mpack and munpack MIME e-mail utilities
Summary(pl):	mpack i munpack - narzêdzia MIME do poczty elektronicznej
Name:		mpack
Version:	1.5
Release:	9
License:	distributable
Group:		Applications/Mail
Source0:	ftp://ftp.andrew.cmu.edu/pub/mpack/%{name}-%{version}-src.tar.Z
# Source0-md5:	f41f8aa2ae92d90e1ac03291973e65e4
Patch0:		%{name}-tmp.patch
Patch1:		%{name}-MIME_buffer_overflows.patch
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
%patch0 -p1
%patch1 -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mpack munpack $RPM_BUILD_ROOT%{_bindir}
install unixpk.man $RPM_BUILD_ROOT%{_mandir}/man1/mpack.1
install unixunpk.man $RPM_BUILD_ROOT%{_mandir}/man1/munpack.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.unix
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
