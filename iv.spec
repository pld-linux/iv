Summary:	ImgView - simple GTK+ image viewer using Imlib
Summary(pl.UTF-8):	ImgView - prosta przeglądarka obrazków oparta na GTK+ i używająca Imliba
Name:		iv
Version:	1.4.2
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	c35e8b210b27acfa5689a8a547eeb947
Patch0:		%{name}-vidmode.patch
URL:		http://wolfpack.twu.net/IV/
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple GTK+ image viewer using Imlib.

%description -l pl.UTF-8
Prosta przeglądarka obrazków oparta na GTK+ i używająca Imliba.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's/!png_check_sig(sig_buf, 8)/png_sig_cmp(sig_buf, 0, 8)/g' iv/imgiopng.c

%build
./configure Linux
%{__make} -C iv \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -ffast-math -Wall \
		-DHAVE_LIBPNG -DHAVE_IMLIB -DINCLUDE_IV_TITLE_IMAGE \
		`gtk-config --cflags` `imlib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C iv \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man1/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*.xpm
%{_mandir}/man1/*.1*
