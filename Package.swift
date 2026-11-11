// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "SmallCurrentsDesign",
    platforms: [.macOS(.v14), .iOS(.v15)],
    products: [
        .library(name: "SmallCurrentsDesign", targets: ["SmallCurrentsDesign"])
    ],
    targets: [
        .target(name: "SmallCurrentsDesign", path: "exports/swift")
    ]
)
