def fill_snappyHexMeshDict(params):
    return   ' // Which of the steps to run '  + '\n' + \
 ' castellatedMesh true; '  + '\n' + \
 ' snap            true; '  + '\n' + \
 ' addLayers       true; '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 ' // Geometry. Definition of all surfaces. All surfaces are of class '  + '\n' + \
 ' // searchableSurface. '  + '\n' + \
 ' // Surfaces are used '  + '\n' + \
 ' // - to specify refinement for any mesh cell intersecting it '  + '\n' + \
 ' // - to specify refinement for any mesh cell inside/outside/near '  + '\n' + \
 ' // - to snap the mesh boundary to the surface '  + '\n' + \
 ' geometry '  + '\n' + \
 ' { '  + '\n' + \
 '     bullet.stl '  + '\n' + \
 '     { '  + '\n' + \
 '         type triSurfaceMesh; '  + '\n' + \
 '         name bullet; '  + '\n' + \
 '  '  + '\n' + \
 '         regions '  + '\n' + \
 '         { '  + '\n' + \
 '             bullet '  + '\n' + \
 '             { '  + '\n' + \
 '                 name bullet; '  + '\n' + \
 '             } '  + '\n' + \
 '         } '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     refinement1 '  + '\n' + \
 '     { '  + '\n' + \
 '         type   sphere; '  + '\n' + \
 '         origin (0 0 0.0025); '  + '\n' + \
 '         radius 0.0075; '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     refinement2 '  + '\n' + \
 '     { '  + '\n' + \
 '         type   cylinder; '  + '\n' + \
 '         point1 (0 0 0); '  + '\n' + \
 '         point2 (0 0 0.03); '  + '\n' + \
 '         radius 0.0075; '  + '\n' + \
 '     } '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 ' // Settings for the castellatedMesh generation. '  + '\n' + \
 ' castellatedMeshControls '  + '\n' + \
 ' { '  + '\n' + \
 '     // Refinement parameters '  + '\n' + \
 '     // ~~~~~~~~~~~~~~~~~~~~~ '  + '\n' + \
 '  '  + '\n' + \
 '     // If local number of cells is >= maxLocalCells on any processor '  + '\n' + \
 '     // switches from from refinement followed by balancing '  + '\n' + \
 '     // (current method) to (weighted) balancing before refinement. '  + '\n' + \
 '     maxLocalCells 100000; '  + '\n' + \
 '  '  + '\n' + \
 '     // Overall cell limit (approximately). Refinement will stop immediately '  + '\n' + \
 '     // upon reaching this number so a refinement level might not complete. '  + '\n' + \
 '     // Note that this is the number of cells before removing the part which '  + '\n' + \
 '     // is not visible from the keepPoint. The final number of cells might '  + '\n' + \
 '     // actually be a lot less. '  + '\n' + \
 '     maxGlobalCells 2000000; '  + '\n' + \
 '  '  + '\n' + \
 '     // The surface refinement loop might spend lots of iterations refining just a '  + '\n' + \
 '     // few cells. This setting will cause refinement to stop if <= minimumRefine '  + '\n' + \
 '     // are selected for refinement. Note: it will at least do one iteration '  + '\n' + \
 '     // (unless the number of cells to refine is 0) '  + '\n' + \
 '     minRefinementCells 10; '  + '\n' + \
 '  '  + '\n' + \
 '     // Number of buffer layers between different levels. '  + '\n' + \
 '     // 1 means normal 2:1 refinement restriction, larger means slower '  + '\n' + \
 '     // refinement. '  + '\n' + \
 '     nCellsBetweenLevels 2; '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '     // Explicit feature edge refinement '  + '\n' + \
 '     // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '  + '\n' + \
 '  '  + '\n' + \
 '     // Specifies a level for any cell intersected by its edges. '  + '\n' + \
 '     // This is a featureEdgeMesh, read from constant/triSurface for now. '  + '\n' + \
 '     features '  + '\n' + \
 '     ( '  + '\n' + \
 '         //{ '  + '\n' + \
 '         //    file "someLine.eMesh"; '  + '\n' + \
 '         //    level 2; '  + '\n' + \
 '         //} '  + '\n' + \
 '     ); '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '     // Surface based refinement '  + '\n' + \
 '     // ~~~~~~~~~~~~~~~~~~~~~~~~ '  + '\n' + \
 '  '  + '\n' + \
 '     // Specifies two levels for every surface. The first is the minimum level, '  + '\n' + \
 '     // every cell intersecting a surface gets refined up to the minimum level. '  + '\n' + \
 '     // The second level is the maximum level. Cells that see multiple '  + '\n' + \
 '     // intersections where the intersections make an '  + '\n' + \
 '     // angle > resolveFeatureAngle get refined up to the maximum level. '  + '\n' + \
 '  '  + '\n' + \
 '     refinementSurfaces '  + '\n' + \
 '     { '  + '\n' + \
 '         bullet '  + '\n' + \
 '         { '  + '\n' + \
 '             // Surface-wise min and max refinement level '  + '\n' + \
 '             level (4 4); '  + '\n' + \
 '         } '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     // Resolve sharp angles '  + '\n' + \
 '     resolveFeatureAngle -1; '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '     // Region-wise refinement '  + '\n' + \
 '     // ~~~~~~~~~~~~~~~~~~~~~~ '  + '\n' + \
 '  '  + '\n' + \
 '     // Specifies refinement level for cells in relation to a surface. One of '  + '\n' + \
 '     // three modes '  + '\n' + \
 '     // - distance. levels specifies per distance to the surface the '  + '\n' + \
 '     //   wanted refinement level. The distances need to be specified in '  + '\n' + \
 '     //   descending order. '  + '\n' + \
 '     // - inside. levels is only one entry and only the level is used. All '  + '\n' + \
 '     //   cells inside the surface get refined up to the level. The surface '  + '\n' + \
 '     //   needs to be closed for this to be possible. '  + '\n' + \
 '     // - outside. Same but cells outside. '  + '\n' + \
 '  '  + '\n' + \
 '     refinementRegions '  + '\n' + \
 '     { '  + '\n' + \
 '         refinement1 '  + '\n' + \
 '         { '  + '\n' + \
 '             mode inside; '  + '\n' + \
 '             levels ((0.0 3)); '  + '\n' + \
 '         } '  + '\n' + \
 '         refinement2 '  + '\n' + \
 '         { '  + '\n' + \
 '             mode inside; '  + '\n' + \
 '             levels ((0.0 3)); '  + '\n' + \
 '         } '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '     // Mesh selection '  + '\n' + \
 '     // ~~~~~~~~~~~~~~ '  + '\n' + \
 '  '  + '\n' + \
 '     // After refinement patches get added for all refinementSurfaces and '  + '\n' + \
 '     // all cells intersecting the surfaces get put into these patches. The '  + '\n' + \
 '     // section reachable from the locationInMesh is kept. '  + '\n' + \
 '     // NOTE: This point should never be on a face, always inside a cell, even '  + '\n' + \
 '     // after refinement. '  + '\n' + \
 '     locationInMesh (0 0 -10e-3); '  + '\n' + \
 '  '  + '\n' + \
 '     allowFreeStandingZoneFaces false; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 ' // Settings for the snapping. '  + '\n' + \
 ' snapControls '  + '\n' + \
 ' { '  + '\n' + \
 '     //- Number of patch smoothing iterations before finding correspondence '  + '\n' + \
 '     //  to surface '  + '\n' + \
 '     nSmoothPatch 3; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Relative distance for points to be attracted by surface feature point '  + '\n' + \
 '     //  or edge. True distance is this factor times local '  + '\n' + \
 '     //  maximum edge length. '  + '\n' + \
 '     tolerance 4.0; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Number of mesh displacement relaxation iterations. '  + '\n' + \
 '     nSolveIter 30; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Maximum number of snapping relaxation iterations. Should stop '  + '\n' + \
 '     //  before upon reaching a correct mesh. '  + '\n' + \
 '     nRelaxIter 5; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 ' // Settings for the layer addition. '  + '\n' + \
 ' addLayersControls '  + '\n' + \
 ' { '  + '\n' + \
 '     // Are the thickness parameters below relative to the undistorted '  + '\n' + \
 '     // size of the refined cell outside layer (true) or absolute sizes (false). '  + '\n' + \
 '     relativeSizes true; '  + '\n' + \
 '  '  + '\n' + \
 '     // Per final patch (so not geometry!) the layer information '  + '\n' + \
 '     layers '  + '\n' + \
 '     { '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     // Expansion factor for layer mesh '  + '\n' + \
 '     expansionRatio 1.0; '  + '\n' + \
 '  '  + '\n' + \
 '     // Wanted thickness of final added cell layer. If multiple layers '  + '\n' + \
 '     // is the thickness of the layer furthest away from the wall. '  + '\n' + \
 '     // Relative to undistorted size of cell outside layer. '  + '\n' + \
 '     // See relativeSizes parameter. '  + '\n' + \
 '     finalLayerThickness 0.3; '  + '\n' + \
 '  '  + '\n' + \
 '     // Minimum thickness of cell layer. If for any reason layer '  + '\n' + \
 '     // cannot be above minThickness do not add layer. '  + '\n' + \
 '     // Relative to undistorted size of cell outside layer. '  + '\n' + \
 '     minThickness 0.1; '  + '\n' + \
 '  '  + '\n' + \
 '     // If points get not extruded do nGrow layers of connected faces that are '  + '\n' + \
 '     // also not grown. This helps convergence of the layer addition process '  + '\n' + \
 '     // close to features. '  + '\n' + \
 '     // Note: changed(corrected) w.r.t 1.7.x! (did not do anything in 1.7.x) '  + '\n' + \
 '     nGrow 0; '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '     // Advanced settings '  + '\n' + \
 '  '  + '\n' + \
 '     // When not to extrude surface. 0 is flat surface, 90 is when two faces '  + '\n' + \
 '     // are perpendicular '  + '\n' + \
 '     featureAngle 30; '  + '\n' + \
 '  '  + '\n' + \
 '     // Maximum number of snapping relaxation iterations. Should stop '  + '\n' + \
 '     // before upon reaching a correct mesh. '  + '\n' + \
 '     nRelaxIter 3; '  + '\n' + \
 '  '  + '\n' + \
 '     // Number of smoothing iterations of surface normals '  + '\n' + \
 '     nSmoothSurfaceNormals 1; '  + '\n' + \
 '  '  + '\n' + \
 '     // Number of smoothing iterations of interior mesh movement direction '  + '\n' + \
 '     nSmoothNormals 3; '  + '\n' + \
 '  '  + '\n' + \
 '     // Smooth layer thickness over surface patches '  + '\n' + \
 '     nSmoothThickness 10; '  + '\n' + \
 '  '  + '\n' + \
 '     // Stop layer growth on highly warped cells '  + '\n' + \
 '     maxFaceThicknessRatio 0.5; '  + '\n' + \
 '  '  + '\n' + \
 '     // Reduce layer growth where ratio thickness to medial '  + '\n' + \
 '     // distance is large '  + '\n' + \
 '     maxThicknessToMedialRatio 0.3; '  + '\n' + \
 '  '  + '\n' + \
 '     // Angle used to pick up medial axis points '  + '\n' + \
 '     // Note: changed(corrected) w.r.t 1.7.x! 90 degrees corresponds to 130 '  + '\n' + \
 '     // in 1.7.x. '  + '\n' + \
 '     minMedialAxisAngle 90; '  + '\n' + \
 '  '  + '\n' + \
 '     // Create buffer region for new layer terminations '  + '\n' + \
 '     nBufferCellsNoExtrude 0; '  + '\n' + \
 '  '  + '\n' + \
 '     // Overall max number of layer addition iterations. The mesher will exit '  + '\n' + \
 '     // if it reaches this number of iterations; possibly with an illegal '  + '\n' + \
 '     // mesh. '  + '\n' + \
 '     nLayerIter 50; '  + '\n' + \
 '  '  + '\n' + \
 '     // Max number of iterations after which relaxed meshQuality controls '  + '\n' + \
 '     // get used. Up to nRelaxIter it uses the settings in meshQualityControls, '  + '\n' + \
 '     // after nRelaxIter it uses the values in meshQualityControls::relaxed. '  + '\n' + \
 '     nRelaxedIter 20; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 ' // Generic mesh quality settings. At any undoable phase these determine '  + '\n' + \
 ' // where to undo. '  + '\n' + \
 ' meshQualityControls '  + '\n' + \
 ' { '  + '\n' + \
 '     //- Maximum non-orthogonality allowed. Set to 180 to disable. '  + '\n' + \
 '     maxNonOrtho 65; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Max skewness allowed. Set to <0 to disable. '  + '\n' + \
 '     maxBoundarySkewness 20; '  + '\n' + \
 '     maxInternalSkewness 4; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Max concaveness allowed. Is angle (in degrees) below which concavity '  + '\n' + \
 '     //  is allowed. 0 is straight face, <0 would be convex face. '  + '\n' + \
 '     //  Set to 180 to disable. '  + '\n' + \
 '     maxConcave 80; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Minimum pyramid volume. Is absolute volume of cell pyramid. '  + '\n' + \
 '     //  Set to very negative number (e.g. -1E30) to disable. '  + '\n' + \
 '     minVol 1e-20; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Minimum quality of the tet formed by the face-centre '  + '\n' + \
 '     //  and variable base point minimum decomposition triangles and '  + '\n' + \
 '     //  the cell centre.  Set to very negative number (e.g. -1E30) to '  + '\n' + \
 '     //  disable. '  + '\n' + \
 '     //     <0 = inside out tet, '  + '\n' + \
 '     //      0 = flat tet '  + '\n' + \
 '     //      1 = regular tet '  + '\n' + \
 '     minTetQuality 1e-30; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Minimum face area. Set to <0 to disable. '  + '\n' + \
 '     minArea -1; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Minimum face twist. Set to <-1 to disable. dot product of face normal '  + '\n' + \
 '     //  and face centre triangles normal '  + '\n' + \
 '     minTwist 0.02; '  + '\n' + \
 '  '  + '\n' + \
 '     //- Minimum normalised cell determinant '  + '\n' + \
 '     //  1 = hex, <= 0 = folded or flattened illegal cell '  + '\n' + \
 '     minDeterminant 0.001; '  + '\n' + \
 '  '  + '\n' + \
 '     //- minFaceWeight (0 -> 0.5) '  + '\n' + \
 '     minFaceWeight 0.02; '  + '\n' + \
 '  '  + '\n' + \
 '     //- minVolRatio (0 -> 1) '  + '\n' + \
 '     minVolRatio 0.01; '  + '\n' + \
 '  '  + '\n' + \
 '     //must be >0 for Fluent compatibility '  + '\n' + \
 '     minTriangleTwist -1; '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 '     // Advanced '  + '\n' + \
 '  '  + '\n' + \
 '     //- Number of error distribution iterations '  + '\n' + \
 '     nSmoothScale 4; '  + '\n' + \
 '     //- Amount to scale back displacement at error points '  + '\n' + \
 '     errorReduction 0.75; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 '  '  + '\n' + \
 ' // Advanced '  + '\n' + \
 '  '  + '\n' + \
 ' // Merge tolerance. Is fraction of overall bounding box of initial mesh. '  + '\n' + \
 ' // Note: the write tolerance needs to be higher than this. '  + '\n' + \
 ' mergeTolerance 1e-6; '
