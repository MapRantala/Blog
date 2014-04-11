
Option Strict Off
Option Explicit On

Imports MSFlexGridLib

Friend Class frmDomainSort
	Inherits System.Windows.Forms.Form
	
	' Copyright 2008 ESRI
	' 
	' All rights reserved under the copyright laws of the United States
	' and applicable international laws, treaties, and conventions.
	' 
	' You may freely redistribute and use this sample code, with or
	' without modification, provided you include the original copyright
	' notice and use restrictions.
	' 
	' See use restrictions at <your ArcGIS install location>/developerkit/userestrictions.txt.
	' 
	
	
	
	
	
	Private m_pWork As ESRI.ArcGIS.Geodatabase.IWorkspaceDomains2
	
	'UPGRADE_WARNING: Event cmbDomains.SelectedIndexChanged may fire when form is initialized. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="88B12AE1-6DE0-48A0-86F1-60C0686C026A"'
	Private Sub cmbDomains_SelectedIndexChanged(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles cmbDomains.SelectedIndexChanged
        PopulateGrid()
        'grdDomain.Invalidate()
	End Sub
	
	Private Sub cmdCancel_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles cmdCancel.Click
		'UPGRADE_NOTE: Object m_pWork may not be destroyed until it is garbage collected. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6E35BFF6-CD74-4B09-9689-3E1A43DF8969"'
		m_pWork = Nothing
		Me.Hide()
	End Sub
	
	Private Sub cmdOK_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles cmdOK.Click
		Me.Hide()
	End Sub
	
	Private Sub frmDomainSort_Load(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles MyBase.Load
		On Error GoTo ErrHandler
		If m_pWork Is Nothing Then Exit Sub
		
		Dim pEnum As ESRI.ArcGIS.Geodatabase.IEnumDomain
		Dim pDomain As ESRI.ArcGIS.Geodatabase.IDomain
		'UPGRADE_WARNING: Couldn't resolve default property of object m_pWork.Domains. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
		pEnum = m_pWork.Domains
		pEnum.Reset()
		cmbDomains.Items.Clear()
		pDomain = pEnum.Next
		Do While Not pDomain Is Nothing
			'UPGRADE_WARNING: TypeOf has a new behavior. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="9B7D5ADD-D8FE-4819-A36C-6DEDAF088CC7"'
			If TypeOf pDomain Is ESRI.ArcGIS.Geodatabase.ICodedValueDomain Then
				cmbDomains.Items.Add(pDomain.Name)
			End If
			
			pDomain = pEnum.Next
		Loop 

        cmbDomains.SelectedIndex = 0
        radSortCode.Checked = True
        radSortAscending.Checked = True

        SizeGrid()
        'optSortItem(0).Checked = True
		Exit Sub
ErrHandler: 
		MsgBox("Form_Load - " & Err.Description)
	End Sub
	
	
    Property Workspace() As ESRI.ArcGIS.Geodatabase.IWorkspace
        Get
            Workspace = m_pWork
        End Get
        Set(ByVal Value As ESRI.ArcGIS.Geodatabase.IWorkspace)
            m_pWork = Value
        End Set
    End Property
	
	'UPGRADE_NOTE: Form_Terminate was upgraded to Form_Terminate_Renamed. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="A9E4979A-37FA-4718-9994-97DD76ED70A7"'
	'UPGRADE_WARNING: frmDomainSort event Form.Terminate has a new behavior. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6BA9B8D2-2A32-4B6E-8D36-44949974A5B4"'
	Private Sub Form_Terminate_Renamed()
		'UPGRADE_NOTE: Object m_pWork may not be destroyed until it is garbage collected. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6E35BFF6-CD74-4B09-9689-3E1A43DF8969"'
		m_pWork = Nothing
	End Sub
	
	Private Sub frmDomainSort_FormClosed(ByVal eventSender As System.Object, ByVal eventArgs As System.Windows.Forms.FormClosedEventArgs) Handles Me.FormClosed
		'UPGRADE_NOTE: Object m_pWork may not be destroyed until it is garbage collected. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6E35BFF6-CD74-4B09-9689-3E1A43DF8969"'
		m_pWork = Nothing
	End Sub
	
	'UPGRADE_WARNING: Event optSortItem.CheckedChanged may fire when form is initialized. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="88B12AE1-6DE0-48A0-86F1-60C0686C026A"'
    Private Sub optSortItem_CheckedChanged(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles radSortAscending.CheckedChanged, radSortDescending.CheckedChanged, radSortCode.CheckedChanged, radSortDescription.CheckedChanged
        If eventSender.Checked Then
            'Dim Index As Short = optSortItem.GetIndex(eventSender)
            SortGrid()
        End If
    End Sub
	
    ''UPGRADE_WARNING: Event optSortType.CheckedChanged may fire when form is initialized. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="88B12AE1-6DE0-48A0-86F1-60C0686C026A"'
    'Private Sub optSortType_CheckedChanged(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles optSortType.CheckedChanged
    '	If eventSender.Checked Then
    '		Dim Index As Short = optSortType.GetIndex(eventSender)
    '		SortGrid()
    '	End If
    'End Sub
	
	Private Sub PopulateGrid()
		On Error GoTo ErrHandler
		'Routine for populating the Grid based on the selected domain
        grdDomain.Rows.Clear()

        ' Create an unbound DataGridView by declaring a column count.
        grdDomain.ColumnCount = 2
        grdDomain.ColumnHeadersVisible = True

        ' Set the column header style.
        Dim columnHeaderStyle As New Windows.Forms.DataGridViewCellStyle
        'columnHeaderStyle.BackColor = Color.Beige
        'columnHeaderStyle.Font = New Font("Verdana", 10, FontStyle.Bold)
        grdDomain.ColumnHeadersDefaultCellStyle = columnHeaderStyle

        ' Set the column header names.
        grdDomain.Columns(0).Name = "Code"
        'grdDomain.Columns(0).SortMode = Windows.Forms.DataGridViewColumnSortMode.NotSortable
        grdDomain.Columns(1).Name = "Description"
        'grdDomain.Columns(1).SortMode = Windows.Forms.DataGridViewColumnSortMode.NotSortable
		
		'Get the domain
		Dim pCoded As ESRI.ArcGIS.Geodatabase.ICodedValueDomain
		Dim lLoop As Integer
		'UPGRADE_WARNING: Couldn't resolve default property of object m_pWork.DomainByName. Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
		pCoded = m_pWork.DomainByName(cmbDomains.Text)
		If pCoded Is Nothing Then
			MsgBox("Could not find domain, something is wrong in PopulateGrid routine!!")
			Exit Sub
		End If
		
        'Populate the grid

        For lLoop = 0 To pCoded.CodeCount - 1
            'UPGRADE_WARNING: Couldn't resolve default property of object pCoded.Value(). Click for more: 'ms-help://MS.VSCC.v90/dv_commoner/local/redirect.htm?keyword="6A50421D-15FE-4896-8A1B-2EC21E9037B2"'
            'grdDomain.AddItem(pCoded.Value(lLoop) & Chr(9) & pCoded.Name(lLoop))
            grdDomain.Rows.Add(pCoded.Value(lLoop), pCoded.Name(lLoop)) '2Done: Finish
        Next lLoop

        SortGrid()

		Exit Sub
ErrHandler: 
		MsgBox("frmDomainSort_PopulateGrid - " & Err.Description)
	End Sub
    Private Sub SizeGrid()

        'Resize the grid
        Dim maxCodeWidth As Integer = 8
        Dim maxValueWidth As Integer = 15
        Dim iRow As System.Windows.Forms.DataGridViewRow
        For Each iRow In grdDomain.Rows

            If (iRow.Cells.Item(0).Value.ToString.Length > maxCodeWidth) Then
                maxCodeWidth = iRow.Cells.Item(0).Value.ToString.Length
            End If

            If (iRow.Cells.Item(1).Value.ToString.Length > maxValueWidth) Then
                maxValueWidth = iRow.Cells.Item(1).Value.ToString.Length
            End If
        Next iRow

        '** Formula is based on 34 = amount Dialog width > DataGridViewWidth, 100 = First psuedo-column width, 5 = character width to size ratio
        Dim newWidth As Integer = 34 + ((20 + (maxCodeWidth * 5)) + (20 + (maxValueWidth * 5)))
        If (newWidth < 275) Then
            newWidth = 275
        End If
        Me.Width = newWidth
        grdDomain.Columns(0).Width = 20 + (maxCodeWidth * 5)
        grdDomain.Columns(1).Width = 20 + (maxValueWidth * 5)
        grdDomain.Columns(0).SortMode = Windows.Forms.DataGridViewColumnSortMode.Programmatic
        grdDomain.Columns(1).SortMode = Windows.Forms.DataGridViewColumnSortMode.Programmatic
        'grdDomain.Invalidate()
    End Sub
	Private Sub SortGrid()
		'Routine for sorting the domain values in the grid based on the option settings
        On Error GoTo ErrHandler

        If radSortCode.Checked Then 'Code sort
            If (radSortAscending.Checked) Then
                grdDomain.Sort(grdDomain.Columns(0), ComponentModel.ListSortDirection.Ascending)
            Else
                grdDomain.Sort(grdDomain.Columns(0), ComponentModel.ListSortDirection.Descending)
            End If
        Else 'Description sort
            If (radSortAscending.Checked) Then
                grdDomain.Sort(grdDomain.Columns(1), ComponentModel.ListSortDirection.Ascending)
            Else
                grdDomain.Sort(grdDomain.Columns(1), ComponentModel.ListSortDirection.Descending)
            End If
        End If

        Exit Sub
ErrHandler:
        MsgBox("SortGrid - " & Err.Description)
    End Sub

    Private Sub grdDomain_SizeChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles grdDomain.SizeChanged
        If (grdDomain.ColumnCount > 1) Then
            Dim grdWidth As Integer = grdDomain.Width
            Dim col1Width As Integer = grdDomain.Columns(0).Width
            Dim col2Width As Integer = grdDomain.Columns(1).Width

            Dim newCol1Width As Integer = grdWidth * (col1Width / (col1Width + col2Width))
            grdDomain.Columns(0).Width = newCol1Width
            grdDomain.Columns(1).Width = grdWidth - newCol1Width
        End If
    End Sub
End Class