import sbt.Keys._

lazy val root = (project in file(".")).
  settings(
    name := "SparkWordCount",
    version := "1.0",
    scalaVersion := "2.11.8",
    mainClass in Compile := Some("SparkWordCount")
  )

exportJars := true
fork := true

// additional libraries
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.1" % "provided",
  "org.apache.spark" %% "spark-streaming" % "1.6.1",
  "org.apache.spark" %% "spark-mllib" % "1.6.1"
)