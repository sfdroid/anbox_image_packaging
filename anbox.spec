Name:       anbox-sailfishos-image
Summary:    Anbox ARM squashfs image with sfdroid changes
Version:    0.0.1
Release: 2
Group:      System/Applications
License:    LICENSE
URL:        https://github.com/sfdroid
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: squashfs-tools

%description
Anbox ARM squashfs image with sfdroid changes

%build

%install
%define anbox_image_dir /var/lib/anbox
mkdir -p %{buildroot}/%{anbox_image_dir}
cp anbox/android.img %{buildroot}/%{anbox_image_dir}

%files
%defattr(444,root,root,444)
%{_sharedstatedir}/anbox/android.img

