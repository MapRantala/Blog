'**** Version 1.1 3/21/2012
'     Add a Try/Catch in GetFirstCVDforWorkspace to catch an exception when user has an open OLE connection
'

Public Class btnDomainSorter
    Inherits ESRI.ArcGIS.Desktop.AddIns.Button

    Public Sub New()

    End Sub

    Protected Overrides Sub OnClick()
        '
        '  TODO: Sample code showing how to access button host
        '
        My.ArcCatalog.Application.CurrentTool = Nothing
        OnClickAction()

    End Sub

    Protected Overrides Sub OnUpdate()
        Enabled = GetFirstCVDforWorkspace(False)
    End Sub
    Private Function GetFirstCVDforWorkspace(ByVal pVerbose As Boolean, Optional ByRef pWork As ESRI.ArcGIS.Geodatabase.IWorkspaceDomains2 = Nothing, Optional ByRef pDomain As ESRI.ArcGIS.Geodatabase.IDomain = Nothing) As Boolean
        '
        '  TODO: Sample code showing how to access button host
        '


        Dim pObj As ESRI.ArcGIS.Catalog.IGxObject
        'Dim pWork As ESRI.ArcGIS.Geodatabase.IWorkspaceDomains2
        Dim pGxData As ESRI.ArcGIS.Catalog.IGxDatabase
        'Dim pObjectTest As Object = My.ArcCatalog '.SelectedOBject
        Dim pGxApplication As ESRI.ArcGIS.CatalogUI.IGxApplication = CType(My.ArcCatalog.Application, ESRI.ArcGIS.CatalogUI.IGxApplication)

        pObj = pGxApplication.SelectedObject

        'UPGRADE_WARNING: TypeOf has a new behavior. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="9B7D5ADD-D8FE-4819-A36C-6DEDAF088CC7"'
        If Not TypeOf pObj Is ESRI.ArcGIS.Catalog.IGxDatabase Then Exit Function

        Dim pEnum As ESRI.ArcGIS.Geodatabase.IEnumDomain
        'Dim pDomain As ESRI.ArcGIS.Geodatabase.IDomain
        Dim bFlag As Boolean
        pGxData = CType(pObj, ESRI.ArcGIS.Catalog.IGxDatabase)
        pWork = CType(pGxData.Workspace, ESRI.ArcGIS.Geodatabase.IWorkspaceDomains2)
        'UPGRADE_WARNING: Couldn't resolve default property of object pWork.Domains. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
        Try
            pEnum = pWork.Domains


            If pEnum Is Nothing Then
                If (pVerbose) Then
                    MsgBox("No coded-value domains to sort.")
                End If

                Return False
            End If

            'Check for coded-value domain
            pEnum.Reset()
            bFlag = False
            pDomain = pEnum.Next
            Do While Not pDomain Is Nothing
                'UPGRADE_WARNING: TypeOf has a new behavior. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="9B7D5ADD-D8FE-4819-A36C-6DEDAF088CC7"'
                If TypeOf pDomain Is ESRI.ArcGIS.Geodatabase.ICodedValueDomain Then
                    bFlag = True
                    Exit Do
                End If
                pDomain = pEnum.Next
            Loop
            If Not bFlag Then
                If (pVerbose) Then
                    MsgBox("No coded-value domains to sort.")
                End If

                Return False
            End If
        Catch ex As Exception
            Return False
        End Try

        Return True

    End Function
    Protected Sub OnClickAction()
        On Error GoTo ErrHandler

        Dim pWork As ESRI.ArcGIS.Geodatabase.IWorkspaceDomains2
        Dim pDomain As ESRI.ArcGIS.Geodatabase.IDomain

        If (GetFirstCVDforWorkspace(True, pWork, pDomain)) Then

            Dim pfrmDomainSort As frmDomainSort = New frmDomainSort
            pfrmDomainSort.Workspace = CType(pWork, ESRI.ArcGIS.Geodatabase.IWorkspace)
            pfrmDomainSort.ShowDialog()
            If pfrmDomainSort.Workspace Is Nothing Then
                pfrmDomainSort.Close()
                Exit Sub 'Cancel was pressed
            End If

            Dim pCoded As ESRI.ArcGIS.Geodatabase.ICodedValueDomain
            Dim lLoop As Integer
            Dim vValue As Object
            'Dim vCode As String
            'Dim vDescription As String

            'UPGRADE_WARNING: Couldn't resolve default property of object pWork.DomainByName. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
            pDomain = pWork.DomainByName(pfrmDomainSort.cmbDomains.Text)
            If pDomain Is Nothing Then Exit Sub

            pCoded = CType(pDomain, ESRI.ArcGIS.Geodatabase.ICodedValueDomain)

            'Drop the domain items
            For lLoop = 0 To pCoded.CodeCount - 1
                pCoded.DeleteCode(pCoded.Value(0))
            Next lLoop

            'Add the domains back in
            For lLoop = 0 To pfrmDomainSort.grdDomain.Rows.Count - 1

                'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                vValue = pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(0).Value.ToString 'pfrmDomainSort.grdDomain.Text
                'vCode = pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(0).Value.ToString

                '*Rantala pfrmDomainSort.grdDomain.Col = 1
                'pfrmDomainSort.grdDomain.CurrentCell = pfrmDomainSort.grdDomain(0, 1)
                'vDescription = pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString

                If pDomain.FieldType = ESRI.ArcGIS.Geodatabase.esriFieldType.esriFieldTypeDouble Then
                    'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                    pCoded.AddCode(CDbl(vValue), pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString) 'pfrmDomainSort.grdDomain.Text)
                ElseIf pDomain.FieldType = ESRI.ArcGIS.Geodatabase.esriFieldType.esriFieldTypeInteger Then
                    'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                    pCoded.AddCode(CInt(vValue), pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString) 'pfrmDomainSort.grdDomain.Text)
                ElseIf pDomain.FieldType = ESRI.ArcGIS.Geodatabase.esriFieldType.esriFieldTypeSmallInteger Then
                    'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                    pCoded.AddCode(CShort(vValue), pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString) 'pfrmDomainSort.grdDomain.Text)
                ElseIf pDomain.FieldType = ESRI.ArcGIS.Geodatabase.esriFieldType.esriFieldTypeDate Then
                    'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                    pCoded.AddCode(CDate(vValue), pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString) 'pfrmDomainSort.grdDomain.Text)
                ElseIf pDomain.FieldType = ESRI.ArcGIS.Geodatabase.esriFieldType.esriFieldTypeSingle Then
                    'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                    pCoded.AddCode(CSng(vValue), pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString) 'pfrmDomainSort.grdDomain.Text)
                ElseIf pDomain.FieldType = ESRI.ArcGIS.Geodatabase.esriFieldType.esriFieldTypeString Then
                    'UPGRADE_WARNING: Couldn't resolve default property of object vValue. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
                    'MsgBox(CStr(vValue).ToString + " " + pfrmDomainSort.grdDomain.Text.ToString + vbNewLine + "Code: " + vCode + vbNewLine + "Desc: " + vDescription)
                    pCoded.AddCode(CStr(vValue), pfrmDomainSort.grdDomain.Rows(lLoop).Cells.Item(1).Value.ToString) 'pfrmDomainSort.grdDomain.Text)
                Else
                    MsgBox("Domain FieldType Not supported: " & pDomain.FieldType)
                    Exit Sub
                End If
            Next lLoop

            pWork.AlterDomain(pDomain)
            'UPGRADE_NOTE: Object frmDomainSort.Workspace may not be destroyed until it is garbage collected. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6E35BFF6-CD74-4B09-9689-3E1A43DF8969"'
            pfrmDomainSort.Workspace = Nothing
            pfrmDomainSort.Close()

            Exit Sub
        End If

ErrHandler:
        MsgBox("DomainSort_OnClick - " & Err.Description)
    End Sub
End Class
