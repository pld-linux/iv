Summary:	ImgView - simple GTK+ image viewer using Imlib
Summary(pl):	ImgView - prosta przegl±darka obrazków oparta na GTK+ i u¿ywaj±ca Imliba
Name:		iv
Version:	0.1.15
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	967febecf125161c792ed05778291b50
URL:		http://wolfpack.twu.net/utilities.html#iv
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple GTK+ image viewer using Imlib.

%description -l pl
Prosta przegl±darka obrazków oparta na GTK+ i u¿ywaj±ca Imliba.

%prep
%setup -q

%build
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
