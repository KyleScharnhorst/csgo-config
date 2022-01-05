param(
   [String]$csgoPath
)

$cfgSubPath = "\csgo\cfg\"

if ([string]::IsNullOrEmpty($csgoPath)) {
    echo ' '
    echo 'Run with elevated privileges.'
    echo 'Run this script in the same directory as the .cfg files.'
    echo 'Please provide the full path to your csgo directory. Something like: "C:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive"'
    echo 'Example usage:'
    echo '.\create_symlinks.ps1 "C:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive"'
}

echo "Appending config path"
if ($csgoPath.EndsWith("\")) {
    $cfgPath = $csgoPath + ($cfgSubPath.Substring(1, $cfgSubPath.Length - 1))
} else {
    $cfgPath = $csgoPath + $cfgSubPath
}

echo "Complete config path: $cfgPath"

if (Test-Path -Path $cfgPath) {
    echo "Path is valid"
} else {
    echo "This path is invalid."
    exit 1
}

#New-Item -ItemType SymbolicLink -Path "Link" -Target "Target"

Get-ChildItem ".\" -Filter *.cfg | 
Foreach-Object {
    $symlinkPath = $cfgPath + $_.Name
    echo "Creating symlink: $symlinkPath"
    $result = New-Item -ItemType SymbolicLink -Path $symlinkPath -Target $_.FullName
    echo "Created symlink: $result"
}