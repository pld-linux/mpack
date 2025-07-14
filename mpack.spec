Summary:	mpack and munpack MIME e-mail utilities
Summary(pl.UTF-8):	mpack i munpack - narzędzia MIME do poczty elektronicznej
Name:		mpack
Version:	1.6
Release:	4
License:	distributable
Group:		Applications/Mail
Source0:	ftp://ftp.andrew.cmu.edu/pub/mpack/%{name}-%{version}.tar.gz
# Source0-md5:	a70fa5afa76539a9afb70b9d81568fe8
Patch0:		%{name}-tmp.patch
Patch1:		%{name}-gentoo.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpack and munpack are utilities for encoding and decoding
(respectively) binary files in MIME (Multipurpose Internet Mail
Extensions) format mail messages. For compatibility with older forms
of transferring binary files, the munpack program can also decode
messages in split-uuencoded format. The Macintosh version can also
decode messages in split-BinHex format. Using mpack you can easily
send files via mail.

%description -l pl.UTF-8
Programy mpack i munpack służą do kodowania i dekodowania
(rekursywnie) plików binarnych w formacie MIME (Multipurpose Internet
Mail Extensions) poczty elektronicznej. Dla zachowania kompatybilności
program munpack także potrafi dekodować listy w formacie
split-uuencoded. Za pomocą programu mpack można łatwo (z linii
poleceń) wysyłać pliki pocztą.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal} -I cmulocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.unix
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
